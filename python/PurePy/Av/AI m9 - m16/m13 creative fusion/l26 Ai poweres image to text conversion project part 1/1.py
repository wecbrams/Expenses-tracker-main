from config import HF_API_KEY
import requests
from PIL import Image
import io
import os
import json
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Utility function for API requests
# -----------------------------------
def query_hf_api(api_url, payload=None, method="post"):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}

    response = requests.post(api_url, headers=headers, json=payload) \
        if method.lower() == "post" else \
        requests.get(api_url, headers=headers, params=payload)

    if response.status_code != 200:
        raise Exception(response.text)

    return response.content


# -----------------------------------
# Generate basic caption from image
# -----------------------------------
def get_basic_caption(image):
    print(Fore.YELLOW + "📷 Generating basic caption...")

    api_url = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"

    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(api_url, headers=headers, data=buffer.read())
    result = response.json()

    return result[0]["generated_text"]


# -----------------------------------
# Generate expanded text using GPT-2
# -----------------------------------
def generate_text(prompt, max_new_tokens):
    api_url = "https://api-inference.huggingface.co/models/gpt2"
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": max_new_tokens}}

    response = query_hf_api(api_url, payload)
    data = json.loads(response.decode())

    return data[0]["generated_text"]


# -----------------------------------
# Truncate text to word limit
# -----------------------------------
def truncate_text(text, limit):
    words = text.split()
    return " ".join(words[:limit])


# -----------------------------------
# Menu display
# -----------------------------------
def print_menu():
    print(Fore.GREEN + """
================ IMAGE TO TEXT =================
1. Caption (5 words)
2. Description (30 words)
3. Summary (50 words)
4. Exit
==============================================
""")


# -----------------------------------
# Main program
# -----------------------------------
def main():
    image_path = input(Fore.BLUE + "Enter image path: ")
    if not os.path.exists(image_path):
        print(Fore.RED + "Image not found.")
        return

    image = Image.open(image_path)
    caption = get_basic_caption(image)
    print(Fore.YELLOW + f"\nBasic Caption: {caption}\n")
    while True:
        print_menu()
        choice = input("Choose option: ")

        if choice == "1":
            print(truncate_text(caption, 5))
        elif choice == "2":
            text = generate_text(f"Expand this caption into 30 words: {caption}", 40)
            print(truncate_text(text, 30))
        elif choice == "3":
            text = generate_text(f"Summarize this image in 50 words: {caption}", 60)
            print(truncate_text(text, 50))
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
