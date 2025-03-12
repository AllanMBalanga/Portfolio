import requests
from datetime import datetime

#https://pixe.la/v1/users/capyngu/graphs/capyngu1.html

USERNAME = "capyngu"
TOKEN = "qwe3fcxvqdsa"
ID = "capyngu1"
headers = {
    "X-USER-TOKEN":TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"

}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": ID,
    "name": "Coding Time",
    "unit": "Hr",
    "type": "int",
    "color": "sora"
}


now = datetime.now()
today = now.strftime("%Y%m%d")
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
pixel_params = {
    "date": today,
    "quantity": input("How many minutes did you spend on learning how to code today?")
}

update_endpoint = f"{pixel_endpoint}/20250216"
update_params = {
    "quantity":"24"
}

delete_endpoint = f"{pixel_endpoint}/{today}"

response = requests.post(url=pixel_endpoint,json=pixel_params, headers=headers)
# response = requests.post(url=pixela_endpoint,json=parameters)
# response = requests.put(url=update_endpoint,json=update_params, headers=headers)
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# response = requests.delete(url=delete_endpoint,headers=headers)