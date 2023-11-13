import requests

USERNAME = "pythonstudent01"
TOKEN = "&GsleEgE7F1$MKZ1"
pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": "&GsleEgE7F1$MKZ1",
    "username": "pythonstudent01",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "myfirstgraph",
    "name": "practice graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

GRAPHID = "myfirstgraph"
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

post_config = {
    "date": "20231110",
    "quantity": "4",
}

response = requests.post(url=post_endpoint, json=post_config, headers=headers)

