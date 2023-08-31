import random
import time
import requests
import statistics
import base64


from prometheus_client import CollectorRegistry, Gauge, pushadd_to_gateway
from prometheus_client.exposition import basic_auth_handler, default_handler


class PrometheusServer:
    def __init__(self, **options):
        self.url = options["url"]
        self.push_url = options["push_url"]
        self.username = options.get("username")
        self.password = options.get("password")
        self.query_root = f"{self.url}/api/v1/query"

    def _auth_handler(self, url, method, timeout, headers, data):
        return basic_auth_handler(
            url, method, timeout, headers, data, self.username, self.password
        )

    def get_measure_name(self, branch, name):
        return (
            base64.urlsafe_b64encode(f"{branch}-{name}".encode()).decode().rstrip("=")
        )

    def mean(self, branch, benchmark, field):
        name = self.get_measure_name(branch, benchmark)

        query = 'avg_over_time(%s{name="%s",branch="%s"}[2d])'
        query = query % (name, field, branch)
        try:
            response = requests.get(self.query_root, params={"query": query})
        except Exception:
            return 0

        res = response.json()
        values = [float(r["value"][-1]) for r in res["data"]["result"]]
        return statistics.mean(values)

    def send_measure(self, branch, benchmark, sha, measure, check_previous=None):
        print(f"Sending metrics to {self.push_url}")
        measure_timestamp = time.time()
        previous = {}

        name = self.get_measure_name(branch, benchmark)

        registry = CollectorRegistry()
        g = Gauge(name, name, ["name", "branch", "sha", "when"], registry=registry)

        for field, value in measure.items():
            g.labels(name=field, branch=branch, sha=sha, when=measure_timestamp).set(
                value
            )
            if check_previous is None:
                continue

            previous[field] = (
                value,
                self.mean(check_previous, benchmark, field),
            )

        if self.username is not None:
            auth_handler = self._auth_handler
        else:
            auth_handler = default_handler

        pushadd_to_gateway(
            self.push_url,
            job="dev-push-gateway",
            registry=registry,
            handler=auth_handler,
        )

        return previous


if __name__ == "__main__":
    prom = PrometheusServer(
        url="http://localhost:9090", push_url="http://localhost:9091"
    )

    def measure():
        m = [
            ("speed_1", float(random.randint(20, 24))),
            ("speed_2", float(random.randint(200, 240))),
            ("speed_3", float(random.randint(1, 10))),
        ]
        return dict(m)

    def add_more(i=100):
        for _ in range(i):
            prom.send_measure("main", "speed", "sha", measure())

        for _ in range(i):
            print(prom.send_measure("tarek/feature", "speed", "sha", measure(), "main"))

    add_more(10)
