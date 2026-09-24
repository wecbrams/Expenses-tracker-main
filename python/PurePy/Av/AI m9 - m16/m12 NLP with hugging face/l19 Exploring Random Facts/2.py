import requests
url = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_fact():
    while True:
        response=requests.get(url)

        if response.status_code==200:
            fact_data=response.json()
            fact=fact_data["text"].lower()

            # Check if it's a tech-related
            keywords=["computer","technology", "internet", "software", "hardware", "ai"]
            
            if any(word in fact for word in keywords):
                print(f"Did you know? {fact_data["text"]}")
                break
        else:
            print("Failed to fetch data")
            break
while True:
    user_input=input("Press Enter to get a random fact or 'q' to quit: ") 
    if user_input.lower().strip()=='q':
        print("Goodbye!!!")
        break
    get_random_fact()