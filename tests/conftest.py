from typing import Dict, Any
import pytest
import flask



@pytest.fixture
def mock_flask_request(request) -> flask.Request:
    method = request.param.get("method", "GET")
    path = request.param.get("path", "/")

    return flask.Request.from_values(
        path=path,
        method=method,
    )


@pytest.fixture(params=[
    {"name": "billy"},
    {"name": "billy", "age": 20},
    {}
])
def state_test_case_fixture(request) -> Dict[str, Any]:
    return request.param
