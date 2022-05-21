import requests
import pytest

class TestFirstApi:
    names = [
        ("Vitalii"),
        ("Ilya"),
        ("Tifio"),
        ("")
    ]
    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name': name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is not field 'answer' in the response"
        if len(name) == 0:
            expected_pesponse_text = "Hello, someone"
        else:
            expected_pesponse_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_pesponse_text, "Actual text in the response correct"
