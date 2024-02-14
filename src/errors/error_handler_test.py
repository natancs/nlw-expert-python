from .error_handler import handle_errors
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

MOCK_EXCEPTION = HttpUnprocessableEntityError("error message")


def test_handler_errors_with_unprocessable_entity():
    result = handle_errors(MOCK_EXCEPTION)

    assert result.status_code == 422
    assert result.body == {
        "errors": [{
            "title": "UprocessableEntity",
            "detail": "error message"
        }]
    }


def test_handler_errors_server_error():
    result = handle_errors("server error")

    assert result.status_code == 500
    assert result.body == {
        "errors": [{
            "title": "Server Error",
            "detail": "server error"
        }]
    }
