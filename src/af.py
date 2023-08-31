import os
import json
import requests
import sys


def markdown_table(data, headers):
    n = max(len(str(x)) for line in data for x in line)
    headerLength = len(headers)
    lines = []
    header_line = ""
    for i in range(len(headers)):
        hn = n - len(headers[i])
        header_line += "|" + " " * hn + f"{headers[i]}"
        if i == headerLength - 1:
            header_line += "|"
    lines.append(header_line)

    sep_line = "|"
    for i in range(len(headers)):
        sep_line += "-" * n + "|"
    lines.append(sep_line)

    for row in data:
        line = ""
        for x in row:
            hn = n - len(str(x))
            line += "|" + " " * hn + str(x)
        line += "|"
        lines.append(line)
    return "\n".join(lines)


def comment_pr(comment, repository, pr_number, github_token):
    url = f"https://api.github.com/repos/{repository}/issues/{pr_number}/comments"
    print(f"Calling `{url}`")

    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    data = {
        "body": comment,
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print("Comment created successfully")
    else:
        print(f"Failed to create comment: {response.text}")


def get_change(current, previous):
    if current == previous:
        return "=="
    try:
        val = (current - previous) / previous * 100.0
        return f"{val:.2f}"
    except (ZeroDivisionError, TypeError):
        return "?"


def main():
    if sys.argv[-1] == "--version":
        print("alwaysfast v1")
        return

    metrics_file = os.getenv("METRICS_FILE", "metrics.json")
    main_branch = os.getenv("MAIN_BRANCH", "main")
    current_branch = os.getenv("HEAD_REF", "main")
    pr_number = os.getenv("PR_NUMBER", "")
    sha = os.getenv("GITHUB_SHA")

    if pr_number != "":
        print(f"Working on PR {pr_number}")

    backend = os.getenv("BACKEND", "influxdb")
    if backend == "influxdb":
        from influx import InfluxDBServer

        server = InfluxDBServer(**dict(os.environ))
    elif backend == "prometheus":
        from prom import PrometheusServer

        server = PrometheusServer(**dict(os.environ))
    else:
        raise NotImplementedError(f"Unknown backend: {backend}")

    benchmark = os.getenv("BENCHMARK_NAME", "speeds")
    repository = os.getenv("GITHUB_REPOSITORY")
    gh_token = os.getenv("GITHUB_TOKEN")

    with open(metrics_file) as f:
        measure = [(e["name"], e["value"]) for e in json.loads(f.read())]

    if pr_number == "":
        # metrics for main branch
        server.send_measure(main_branch, benchmark, sha, dict(measure))
    else:
        res = server.send_measure(
            current_branch, benchmark, sha, dict(measure), main_branch
        )

        headers = ["Test", "PR benchmark", "Main benchmark", "%"]
        lines = []
        for test, (pr, main) in res.items():
            lines.append([test, pr, main, get_change(pr, main)])

        table = markdown_table(lines, headers)

        comment = f"""\
        Benchmarks comparison to {main_branch} branch

        {table}

        Happy hacking!
        """

        comment = "\n".join([line.lstrip() for line in comment.split("\n")])
        comment_pr(comment, repository, pr_number, gh_token)


if __name__ == "__main__":
    main()
