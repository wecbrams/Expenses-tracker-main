import requests
from config import keys

api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased"
headers={"Authorization": f"Bearer {keys}"}

text_input = input("Enter the text for sentiment analysis: ")
response = requests.post(api_url, headers=headers, json={"inputs":text_input})

if response.status_code==200:
    result = response.json()
    print(f"Sentiment: {result[0]['label']} with confidence score: {result[0]['score']}")
    
else:
    print(f"error: {response.status_code}")