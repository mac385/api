import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuaWNrbmFtZSI6IlNhbWl0IENoYWt'


headers = {"Authorization": f"Bearer {token}"}
url = "https://mwf.qa.causeway.com/v2/gateway-docs/folder/info?tag=LB0120:ECO1182:45157"

def test_status_code():

    response = requests.get (url , headers = headers)

    assert response.status_code == 200


def test_response_body():

    response = requests.get (url , headers = headers)
    resp_body = response.json ()


    assert resp_body == {
            "nodes": [
                {
                    "_id": "64206d55c280d0ae2da94943" ,
                    "name": "notifications.png" ,
                    "versionId": "64206d55c280d08a7fa94944"
                } ,
                {
                    "_id": "64206d55c280d00ef9a94933" ,
                    "name": "msg_check3.png" ,
                    "versionId": "64206d55c280d0a62aa94934"
                } ,
                {
                    "_id": "64206d55c280d0805da9491d" ,
                    "name": "mwf-4952.png" ,
                    "versionId": "64206d55c280d00f86a9491e"
                }
            ] ,
            "total": 3 ,
            "limit": 1000 ,
            "offset": 0 ,
            "folderId": "64206d46c280d02c86a94882" ,
            "orgId": "4f7709f1-e33f-41e4-aaf9-b30119d9adc7"
        }


def test_response_content():

    response = requests.get (url , headers = headers)
    resp_body = response.json ()

    assert "total" in resp_body


def test_response_count():

    response = requests.get (url , headers = headers)
    resp_body = response.json ()

    assert resp_body ["total"] == 3


def test_header():

    response = requests.get (url , headers = headers)

    assert response.headers["Content-Type"] == "application/json;charset=UTF-8"


def test_negative_status_code():

    response = requests.get (url , headers = headers)

    assert response.status_code != 400


def test_negative_response_count():

    response = requests.get (url , headers = headers)
    resp_body = response.json ()

    assert resp_body ["total"] != 10


def test_response_name2():
    response = requests.get(url, headers=headers)
    resp_body = response.json()

    assert "name" in resp_body["nodes"][0]



def test_response_count2():

    response = requests.get (url , headers = headers)
    resp_body = response.json ()

    assert resp_body["nodes"][0]["name"] == "notifications.png"


