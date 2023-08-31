import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxDBServer:
    def __init__(self, **options):
        self.token = options["INFLUXDB_TOKEN"]
        self.bucket = options["INFLUXDB_BUCKET"]
        self.url = options["INFLUXDB_URL"]
        self.org = options["INFLUXDB_ORG"]
        self.client = InfluxDBClient(url=self.url, org=self.org, token=self.token)

    def mean(self, branch, benchmark, field):
        query = f"""
        from(bucket:"{self.bucket}")
        |> range(start: -30d, stop: now())
        |> filter(fn: (r) => r["branch"] == "{branch}")
        |> filter(fn: (r) => r["_measurement"] == "{benchmark}")
        |> filter(fn: (r) => r["_field"] == "{field}")
        |> sort(columns: ["_stop"], desc: true)
        |> limit(n:10)
        |> mean(column: "_value")
        """
        query_api = self.client.query_api()
        previous = query_api.query(query)
        if len(previous) == 0:
            return None
        if len(previous[0].records) == 0:
            return None

        return previous[0].records[0].values["_value"]

    def send_measure(self, branch, benchmark, sha, measure, check_previous=None):
        print(f"Sending metrics")
        write_api = self.client.write_api(write_options=SYNCHRONOUS)

        previous = {}

        for field, value in measure.items():
            point = (
                Point(benchmark)
                .tag("branch", branch)
                .tag("sha", sha)
                .field(field, value)
            )
            write_api.write(bucket=self.bucket, record=point)

            if check_previous is None:
                continue

            previous[field] = (
                value,
                self.mean(check_previous, benchmark, field),
            )

        return previous
