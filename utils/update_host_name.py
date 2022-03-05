import requests

from json import dumps

header = {"Content-Type": "application/json", "Authorization": ""}

url = "https://api.balena-cloud.com/supervisor/v1/device/host-config"

body = {
    "uuid": "",
    "method": "PATCH",
    "data": {"network": {"hostname": ""}},
}

def update_hostname(uuid, new_hostname, bearer_token):
    header["Authorization"] = "Bearer " + bearer_token
    body["uuid"] = uuid
    body["data"]["network"]["hostname"] = new_hostname
    response = requests.post(url, data=dumps(body), headers=header)
    return response.status_code

if __name__ == "__main__":
    pass
