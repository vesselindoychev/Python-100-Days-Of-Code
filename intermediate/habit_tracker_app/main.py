import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(verbose=True)

user_endpoint = 'https://pixe.la/v1/users'

auth_token = os.environ['AUTH_TOKEN']
auth_username = os.environ['AUTH_USERNAME']

user_params = {
    'token': auth_token,
    'username': auth_username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'

}

# response = requests.post(url=user_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{user_endpoint}/{auth_username}/graphs'

graph_id = os.environ['AUTH_GRAPH_ID']
graph_name = os.environ['AUTH_GRAPH_NAME']
graph_unit = os.environ['AUTH_GRAPH_UNIT']
graph_type = os.environ['AUTH_GRAPH_TYPE']
graph_color = os.environ['AUTH_GRAPH_COLOR']

graph_params = {
    'id': graph_id,
    'name': graph_name,
    'unit': graph_unit,
    'type': graph_type,
    'color': graph_color,
}

headers = {
    'X-USER-TOKEN': auth_token
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

post_graph_endpoint = f"{graph_endpoint}/{graph_id}"

current_date = datetime.now().strftime("%Y%m%d")


post_graph_params = {
    'date': current_date,
    'quantity': '3.1'
}

post_response = requests.post(url=post_graph_endpoint, json=post_graph_params, headers=headers)
print(post_response.text)
