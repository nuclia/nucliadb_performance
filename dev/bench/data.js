window.BENCHMARK_DATA = {
  "lastUpdate": 1675949483454,
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
      },
      {
        "commit": {
          "author": {
            "email": "ferran@nuclia.com",
            "name": "Ferran Llamas",
            "username": "lferran"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "094673dd0f595864e2e0dd7b816a8e24b40ea633",
          "message": "Improvements on node load reporting (#562)\n\n* Squashed\r\n\r\n* Fix tests\r\n\r\n---------\r\n\r\nCo-authored-by: Alexis Le Provost <alexis.leprovost@outlook.com>",
          "timestamp": "2023-02-09T14:20:16+01:00",
          "tree_id": "6823f72cf07184af2c2f2ce0fcf5c71cff6f8ff3",
          "url": "https://github.com/nuclia/nucliadb/commit/094673dd0f595864e2e0dd7b816a8e24b40ea633"
        },
        "date": 1675949483060,
        "tool": "pytest",
        "benches": [
          {
            "name": "nucliadb/tests/benchmarks/test_search.py::test_search_returns_labels",
            "value": 74.42956552538958,
            "unit": "iter/sec",
            "range": "stddev: 0.00017889844852212063",
            "extra": "mean: 13.435521125793457 msec\nrounds: 5"
          },
          {
            "name": "nucliadb/tests/benchmarks/test_search.py::test_search_relations",
            "value": 142.8071800179773,
            "unit": "iter/sec",
            "range": "stddev: 0.00010968460889721766",
            "extra": "mean: 7.00244903564453 msec\nrounds: 5"
          }
        ]
      }
    ]
  }
}