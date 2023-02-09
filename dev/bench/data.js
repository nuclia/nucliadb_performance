window.BENCHMARK_DATA = {
  "lastUpdate": 1675938425943,
  "repoUrl": "https://github.com/nuclia/nucliadb",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "ramon@nuclia.io",
            "name": "Ramon Navarro Bosch",
            "username": "bloodbare"
          },
          "committer": {
            "email": "ramon@nuclia.io",
            "name": "Ramon Navarro Bosch",
            "username": "bloodbare"
          },
          "distinct": true,
          "id": "d19d1318b903b0f69a871f43bea04b78e1c10a25",
          "message": "Fix test",
          "timestamp": "2023-02-09T11:18:34+01:00",
          "tree_id": "e4a1c85d92805139bcb7ab6156b916c52e872559",
          "url": "https://github.com/nuclia/nucliadb/commit/d19d1318b903b0f69a871f43bea04b78e1c10a25"
        },
        "date": 1675938118312,
        "tool": "pytest",
        "benches": [
          {
            "name": "nucliadb/tests/benchmarks/test_search.py::test_search_returns_labels",
            "value": 68.48176450054224,
            "unit": "iter/sec",
            "range": "stddev: 0.00011698806646091496",
            "extra": "mean: 14.602427482604982 msec\nrounds: 5"
          },
          {
            "name": "nucliadb/tests/benchmarks/test_search.py::test_search_relations",
            "value": 128.13602179672588,
            "unit": "iter/sec",
            "range": "stddev: 0.000027569798386079616",
            "extra": "mean: 7.8042067014254055 msec\nrounds: 5"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "ramon@nuclia.io",
            "name": "Ramon Navarro Bosch",
            "username": "bloodbare"
          },
          "committer": {
            "email": "ramon@nuclia.io",
            "name": "Ramon Navarro Bosch",
            "username": "bloodbare"
          },
          "distinct": true,
          "id": "d19d1318b903b0f69a871f43bea04b78e1c10a25",
          "message": "Fix test",
          "timestamp": "2023-02-09T11:18:34+01:00",
          "tree_id": "e4a1c85d92805139bcb7ab6156b916c52e872559",
          "url": "https://github.com/nuclia/nucliadb/commit/d19d1318b903b0f69a871f43bea04b78e1c10a25"
        },
        "date": 1675938425303,
        "tool": "pytest",
        "benches": [
          {
            "name": "nucliadb/search/tests/test_highlight.py::test_highligh_error",
            "value": 4410.782561656566,
            "unit": "iter/sec",
            "range": "stddev: 3.74708783249548e-7",
            "extra": "mean: 226.71713829040527 usec\nrounds: 5"
          }
        ]
      }
    ]
  }
}