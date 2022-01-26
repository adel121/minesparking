import requests
import json

def send_request(context):
	api_url = "http://127.0.0.1:8000/parking/match_cars/"
	headers =  {"Content-Type":"application/json"}
	response = requests.post(api_url, data=json.dumps(context), headers=headers)
	return response


