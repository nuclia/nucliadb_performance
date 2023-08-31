# nucliadb_performance

Github Action for continuous benchmarking.

This action is highly inspired from https://github.com/benchmark-action/github-action-benchmark
but is branch-aware and uses a time-series database.

The key differences are:

- metrics are stored in InfluxDB or Prometheus instead of a single JSON file
- you can run the action from a PR comment to get a diff with `main`
- the diff is made with the 10 last metrics from main to reduce noise and false positives.

Example of comments in the PR:

![PR](example.png)

## How to use

The first step is to generate metrics with your favorite tool.
The results need to be stored in a JSON file. The structure
is dead simple: it has to be a list of elements where each element
is a mapping with a name and a numerical value.

Example:

```json
[
  { "name": "speed_1", "value": 22.0 },
  { "name": "speed_2", "value": 210.0 },
  { "name": "speed_3", "value": 9.0 }
]
```

How you generated that value is up to you. The fanciest
benchmarks will run cycles of 25 runs on bare metal to avoid
noise and false positives, but a simple script that generates
one value can already go a long way.

Once you have that script in your repo, we can plug it into
a Github Action step right before we run `nucliadb_performance`.

The bench will run on main and every PR, allowing you
to track performance regressions (or improvements!)

Example of action file:

```yaml
name: Test Action
on:
  push:
    branches:
      - main
  issue_comment:
    types: [created]

permissions: write-all

jobs:
  check-perf-main:
    if: github.event_name == 'push'
    name: Record performance on main
    runs-on: ubuntu-latest
    steps:
      - name: Checkout the repository
        uses: actions/checkout@v3
      - name: Run the bench
        run: python demo.py
      - name: Check perf
        uses: nuclia/nucliadb_performance@main
        with:
          metrics_file: metrics.json
          influxdb_url: ${{ secrets.INFLUXDB_SERVER }}
          influxdb_token: ${{ secrets.INFLUXDB_TOKEN }}
          influxdb_org: nuclia
          influxdb_bucket: benchmarks
  check-perf-pr:
    if: github.event.issue.pull_request && contains(github.event.comment.body, '/bench')
    runs-on: ubuntu-latest
    name: Check performance on the PR
    steps:
      - name: Get PR branch
        uses: xt0rted/pull-request-comment-branch@v1
        id: comment-branch
      - uses: actions/checkout@v3
        if: success()
        with:
          ref: ${{ steps.comment-branch.outputs.head_ref }}
      - name: Run the bench
        run: python demo.py
      - name: Check perf
        uses: nuclia/nucliadb_performance@main
        with:
          metrics_file: metrics.json
          head_ref: ${{ steps.comment-branch.outputs.head_ref }}
          influxdb_url: ${{ secrets.INFLUXDB_SERVER }}
          influxdb_token: ${{ secrets.INFLUXDB_TOKEN }}
          influxdb_org: nuclia
          influxdb_bucket: benchmarks
```
