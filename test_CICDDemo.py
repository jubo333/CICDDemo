import requests


def test_get_users():
    url = "https://reqres.in/api/users?page=2"
    print(f"Sending request to: {url}")

    response = requests.get(url)

    print("Response status code:", response.status_code)
    print("Response body:", response.json())

    assert response.status_code == 200
    assert "data" in response.json()


if __name__ == "__main__":
    test_get_users()
