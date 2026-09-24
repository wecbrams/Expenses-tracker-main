# joke_fetcher.py
import requests
API_URL = "https://official-joke-api.appspot.com/random_joke"

def get_random_joke():
    """Fetch a random joke from the official joke API and return a string."""
    try:
        resp = requests.get(API_URL, timeout=5)  # send request (5s timeout)
    except requests.RequestException as e:
        # network error or request problem
        return f"Network error: {e}"
    if resp.status_code != 200:
        return f"API error: status code {resp.status_code}"
    try:
        data = resp.json()  # parse JSON into a Python dict
    except ValueError:
        return "Error: Response not valid JSON."
    # Safely get the fields we expect
    setup = data.get("setup")
    punchline = data.get("punchline")
    if not setup or not punchline:
        return "Error: Unexpected API response format."
    return f"{setup}\n→ {punchline}"
def main():
    print("Random Joke Generator (press Enter to get a joke, type 'q' to quit)")
    while True:
        user = input(">> ").strip().lower()
        if user in ("q", "exit"):
            print("Goodbye!")
            break
        joke_text = get_random_joke()
        print("\n" + joke_text + "\n")

if __name__ == "__main__":
    main()
