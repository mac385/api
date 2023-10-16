import requests



token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWZyZXNoX3Rva2VuIjoiQW"

url = 'https://mobile.qa.causeway.com/v3/api/files?documentType=ad_hoc_grn&documentId=04716529-2c14-48ba-8811-2e561a1a7b72&photoIndex=1'
with open('8.png' , 'rb') as photo:
    file = photo.read()

header = {"Authorization": f"Bearer {token}"}


def test_execute_post():
    payload = {"file": ("5.png", file),"Body": ("Form-data") }

    response = requests.post(url, files=payload, headers=header)

    assert response.status_code == 200


def test_execute_post_NEGATIVE():
    payload = {"file": ("9.png" , file) , "Body": ("Form-data")}

    response = requests.post (url , files = payload , headers = header)

    assert response.status_code != 201