# import requests 
# from config import November_22
# def classify_text(text):
#     API_URL="https://router.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
#     headers={"Authorization": f"Bearer{November_22}"}
#     payload={"inputs": text}
#     response=requests.post(API_URL,headers=headers,json=payload)
#     return response.json()
# if __name__=="__main__":
#     sample_text="I love using Hugging Fcae APIS!"
#     result=classify_text(sample_text)
#     print(result)

import requests
from config import November_22   # your API key

def classify_text(text):
    API_URL = "https://router.huggingface.co/pipeline/text-classification/distilbert-base-uncased-finetuned-sst-2-english"

    headers = {
        "Authorization": f"Bearer {November_22}",
        "Content-Type": "application/json"
    }

    payload = {"inputs": text}

    response = requests.post(API_URL, headers=headers, json=payload)

    # Safe JSON handling
    try:
        return response.json()
    except ValueError:
        print("❌ ERROR: Hugging Face returned non-JSON response:")
        print(response.text)
        return None

if __name__ == "__main__":
    sample_text = "I love using Hugging Face APIs!"
    result = classify_text(sample_text)
    print(result)
