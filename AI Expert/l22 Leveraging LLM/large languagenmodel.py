import requests
from colorama import Fore, Style, init
from config import keys

init(autoreset=True)

# Replace this with your actual Hugging Face API key
# HF_API_KEY = "YOUR_HUGGING_FACE_API_KEY"

# Default summarization model
DEFAULT_MODEL = "google/pegasus-xsum"

def build_api_url(model_name):
    """
    Builds the Hugging Face API URL using the model name.
    """
    return f"https://api-inference.huggingface.co/models/{model_name}"


def query(payload, model_name=DEFAULT_MODEL):
    """
    Sends a POST request to the Hugging Face API.
    """
    api_url = build_api_url(model_name)
    headers = {
        "Authorization": f"Bearer {keys}"
    }

    response = requests.post(api_url, headers=headers, json=payload)
    return response.json()


def summarize_text(text, min_length, max_length, model_name=DEFAULT_MODEL):
    """
    Sends text to the API and returns the summarized text.
    """
    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_length,
            "max_length": max_length
        }
    }

    print(Fore.BLUE + Style.BRIGHT +
          f"\n Performing AI summarization using model: {model_name}...")

    result = query(payload, model_name)

    # Check if the response is valid
    if isinstance(result, list) and len(result) > 0 and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print(Fore.RED + "Error in summarization response:")
        print(result)
        return None


# MAIN PROGRAM

if __name__ == "__main__":

    # Ask for the user's name
    print(Fore.YELLOW + Style.BRIGHT +
          "👋 Hi there! What's your name?")
    user_name = input("Your name: ").strip()

    if not user_name:
        user_name = "User"

    print(Fore.GREEN +
          f"\nWelcome, {user_name}! Let's give your text some AI magic ✨")

    # Ask for text input
    print(Fore.YELLOW + Style.BRIGHT +
          "\n📄 Please enter the text you want to summarize:")
    user_text = input().strip()

    if not user_text:
        print(Fore.RED + "❌ No text provided. Exiting program.")
        exit()

    # Ask for model choice
    print(Fore.YELLOW +
          "\n🤖 Enter the model name you want to use")
    print("(e.g. facebook/bart-large-cnn)")
    model_choice = input("Model name (leave blank for default): ").strip()

    if not model_choice:
        model_choice = DEFAULT_MODEL

    # Ask for summarization style
    print(Fore.YELLOW + "\n✏ Choose your summarization style:")
    print("1. Standard Summary (Quick & concise)")
    print("2. Enhanced Summary (More detailed)")

    style_choice = input("Enter 1 or 2: ").strip()

    if style_choice == "2":
        min_length = 80
        max_length = 200
        print(Fore.BLUE +
              "🔍 Using enhanced summarization settings...")
    else:
        min_length = 50
        max_length = 150
        print(Fore.BLUE +
              "⚡ Using standard summarization settings...")

    # Generate summary
    summary = summarize_text(
        user_text,
        min_length,
        max_length,
        model_name=model_choice
    )

    # Display result
    if summary:
        print(Fore.GREEN + Style.BRIGHT +
              f"\n📌 AI Summarizer Output for {user_name}:")
        print(Fore.GREEN + summary)
    else:
        print(Fore.RED + "❌ Failed to generate summary.")
