import os
from nucliadb_performance.metrics import Metrics, METRICS_TOOL


def test_pytest():
    data = os.path.join(os.path.dirname(__file__), "from_pytest.json")

    m = Metrics(data)
    assert m.tool == METRICS_TOOL.PYTEST
    assert "test_search_relations" in m.measures.keys()


def test_custom():
    data = os.path.join(os.path.dirname(__file__), "from_custom.json")

    m = Metrics(data)
    assert m.tool == METRICS_TOOL.CUSTOM
    assert "Labels Index Time" in m.measures.keys()
