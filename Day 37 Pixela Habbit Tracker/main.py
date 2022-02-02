import requests
from datetime import datetime as dt

TOKEN = "Huck^Th!$_She3t_"
USERNAME = "razvan"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Swimming Graph",
    "unit": "m",
    "type": "int",
    "color": "sora",
}
headers = {"X-USER-TOKEN": TOKEN}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

# ADDING A RECORD

post_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = dt.now()
post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "500",
}

post_response = requests.post(url=post_endpoint, json=post_params, headers=headers)
print(post_response.text)

# MODIFYING A RECORD

day_to_edit = "20220116"
put_endpoint = f"{post_endpoint}/{day_to_edit}"
put_params = {"quantity": "450"}

# put_response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(put_response.text)

# DELETING A RECORD

day_to_delete = "20220116"
delete_endpoint = f"{post_endpoint}/{day_to_delete}"

# delete_response = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_response.text)

