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
