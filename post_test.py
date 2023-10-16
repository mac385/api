import requests
import uuid


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuaWNrbmFtZSI6IlNhb"

url = 'https://mwf.qa.causeway.com/v2/gateway-docs/files/v2'
with open('8.png' , 'rb') as photo:
    file = photo.read()

header = {"Authorization": f"Bearer {token}"}


def test_execute_post():
    payload = {"file": ("8.png", file), "contract": (None, "LB0120"),
               "orderNo": (None, "ECO1032/450067"), "status": (None, "Delivered"), "notes": (None, "some notes"),
               "name": (None, str(uuid.uuid4()))}

    response = requests.post(url, files=payload, headers=header)

    assert response.status_code == 201