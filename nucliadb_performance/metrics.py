import json
from enum import Enum


class METRICS_TOOL(Enum):
    UNKNOWN = 0
    CUSTOM = 1
    PYTEST = 2


class Metrics:
    def __init__(self, metrics_file=None):
        self.tool = METRICS_TOOL.UNKNOWN
        self.metrics_file = metrics_file

        if metrics_file is not None:
            with open(metrics_file) as f:
                self.data = json.loads(f.read())

            measures = []
            if "benchmarks" in self.data:
                for bench in self.data["benchmarks"]:
                    name = bench["name"]
                    value = bench["stats"]["mean"]

                    measures.append((name, value))
                self.tool = METRICS_TOOL.PYTEST
            else:
                measures = [(e["name"], e["value"]) for e in self.data]
                self.tool = METRICS_TOOL.CUSTOM
            self.measures = dict(measures)
        else:
            self.measures = {}
