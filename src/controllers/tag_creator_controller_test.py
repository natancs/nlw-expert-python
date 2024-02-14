from unittest.mock import patch
from src.drivers.barcode_handler import BarcodeHandler
from .tag_creator_controller import TagCreatorController

MOCK_VALUE = "image_path"


@patch.object(BarcodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    mock_create_barcode.return_value = MOCK_VALUE
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(MOCK_VALUE)

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result["data"]["type"] == "Tag Image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f'{MOCK_VALUE}.png'


@patch.object(TagCreatorController, "_TagCreatorController__create_tag")
def test_create_tag_called(mock_create_tag):
    mock_create_tag.return_value = "Method_Mocked"
    tag_creator_controller = TagCreatorController()

    response = tag_creator_controller.create(MOCK_VALUE)
    mock_create_tag.assert_called_once()

    assert response == {
        "data": {
            "type": "Tag Image",
            "count": 1,
            "path": 'Method_Mocked.png'
        }
    }


@patch.object(TagCreatorController, "_TagCreatorController__format_response")
@patch.object(TagCreatorController, "_TagCreatorController__create_tag")
def test_format_response_called(mock_format_response, mock_create_tag):
    mock_create_tag.return_value = "Method_Mocked"
    mock_format_response.return_value = "Method_Mocked"
    tag_creator_controller = TagCreatorController()

    response = tag_creator_controller.create(MOCK_VALUE)
    mock_format_response.assert_called_once()

    assert response == "Method_Mocked"
