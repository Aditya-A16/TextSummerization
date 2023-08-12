import requests
#from config import api_token
import os

api_token = os.environ.get('API_TOKEN')
model_id = "sshleifer/distilbart-cnn-12-6"

def query(payload, model_id, api_token):
	headers = {"Authorization": f"Bearer {api_token}"}	
    
	API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()



#pi_token = "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"


def summerizer(para):
    data = query(para, model_id, api_token)   
    text = data[0]['summary_text'] 
    return text
