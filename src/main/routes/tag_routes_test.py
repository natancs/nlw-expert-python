import requests

BASE_URL = 'http://0.0.0.0:3000'


def test_post_create_tag():
    new_tag = {
        "product_code": "testuhuu"
    }
    response = requests.post(f'{BASE_URL}/create_tag', json=new_tag)
    assert response.status_code == 201

    response_body = response.json()

    assert response_body == {
        "data": {
            "type": "Tag Image",
            "count": 1,
            "path": f'{new_tag["product_code"]}.png'
        }}


def test_post_create_tag_with_error():
    new_tag = {
        "product_cod": "testuhuu"
    }
    response = requests.post(f'{BASE_URL}/create_tag', json=new_tag)
    assert response.status_code == 422

    response_body = response.json()

    assert response_body == {
        "errors": [
            {
                "detail": {
                    "product_cod": [
                        "unknown field"
                    ],
                    "product_code": [
                        "required field"
                    ]
                },
                "title": "UprocessableEntity"
            }
        ]
    }
