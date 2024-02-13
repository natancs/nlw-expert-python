from unittest.mock import patch
from src.controllers.tag_creator_controller import TagCreatorController
from src.views.http_types.http_request import HttpRequest
from .tag_creator_view import TagCreatorView


class MockTagCreatorController:
    def create(self, product_code: str):
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{product_code}.png'
            }
        }


@patch.object(TagCreatorController, "create")
def test_tag_creator_view(mock_create):
    mock_create.return_value = MockTagCreatorController().create(product_code="test")
    tag_creator_view = TagCreatorView()
    http_request = HttpRequest(body={
        "product_code": "test"
    })
    response = tag_creator_view.validate_and_create(http_request=http_request)
    assert response.body == {
        "data": {
            "type": "Tag Image",
            "count": 1,
            "path": 'test.png'
        }
    }
    assert response.status_code == 201
