import requests
import uuid
from multiprocessing import Process

url = 'https://mobile.qa.causeway.com/v3/api/files?documentType=ad_hoc_grn&documentId=04716529-2c14-48ba-8811-2e561a1a7b73&photoIndex=1'
with open('8.png', 'rb') as photo:
    file = photo.read()

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWZyZXNoX3Rva2VuIjoiYUxwN3dETnhGWHMzTEtDTGRvMDg5N3FxcDY0WUZJUUJnVzlRMFE2M0JxQ2ZKM3BvWjNQeHNrRGVJUFRUWGMzYyIsImlhdCI6MTY5Mzk4OTEwNCwiaXNzIjoiaHR0cHM6XC9cL2xvZ2luLnFhLmNhdXNld2F5LmNvbTo0NDMiLCJhdWQiOiJjbWYtYWRtaW4tY29uc29sZSIsIm5hbWUiOiJTYW1pdCBDaGFrcmFib3J0eSIsImVtYWlsIjoiYmFsLXNhbWl0LmNoYWtyYWJvcnR5QGNhdXNld2F5LmNvbSIsImdpdmVuX25hbWUiOiJTYW1pdCIsImFjY2Vzc190b2tlbiI6IjhpOEh0TmM3Z0xXOTRneXI3a3p3VWdEYTQ2MCIsImZhbWlseV9uYW1lIjoiQ2hha3JhYm9ydHkiLCJleHAiOjE2OTQwMTc5MDQsImxpY2Vuc2VzIjp7IkNNUF9TUFJFQURTSEVFVEVYUE9SVCI6dHJ1ZSwiQ01QX1JFUE9SVERFU0lHTkVSIjp0cnVlLCJDTVBfU1BSRUFEU0hFRVRJTVBPUlQiOnRydWV9LCJzdWIiOiI0ZTkzMzk0NS05MWZkLTQ0ZGYtYWY1ZC1jZjdlYjc3ODhhYTIiLCJhcHBfbmFtZSI6ImFkbWluIiwib3JnYW5pemF0aW9uIjp7ImlkIjoiYTIyNTkxNTMtOGNiYy00MTlhLWFiMmItOTZiN2I5M2MzOWVmIiwibmFtZSI6IkJhbGZvdXIgQmVhdHR5IEdyb3VwIExpbWl0ZWQifX0.5h5e1Asjxv_pwbZqQCBuQO8LdXTWIyy2nUHqEgmS2JA"
header = {"Authorization": f"Bearer {token}"}


def execute_post():
    payload = {"file": ("8.png", file), "Body": ("Form-data")}
    response = requests.post(url, files=payload, headers=header)
    print (response.status_code, response.content)

exec_type = 'Seq'
api_posts = 2


if __name__ == '__main__':
    if exec_type == 'Sim':
        api_calls = []

        for i in range(api_posts):
            api_calls.append(Process(target=execute_post))


        for ex in api_calls:
            print(ex)
            ex.start()

        for index, ex in enumerate(api_calls):
            print(index)
            ex.join()
    else:
        for i in range(api_posts):
            execute_post()