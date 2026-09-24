import requests
import random
import html

API_BASE = "https://opentdb.com/api.php"

def fetch_trivia(amount=5, category=None, difficulty=None, qtype="multiple"):
    """
    Fetch trivia questions from Open Trivia DB.
    Returns a list of question dicts on success, or None on failure.
    """
    params = {"amount": amount, "type": qtype}
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty

    try:
        resp = requests.get(API_BASE, params=params, timeout=8)
    except requests.RequestException as e:
        print(f"[Network error] Could not reach API: {e}")
        return None

    if resp.status_code != 200:
        print(f"[API error] Status code: {resp.status_code}")
        return None

    try:
        data = resp.json()
    except ValueError:
        print("[Parse error] Response was not valid JSON.")
        return None

    # API returns response_code: 0 means success
    if data.get("response_code") != 0:
        print(f"[API] No questions returned (response_code={data.get('response_code')}).")
        return None

    return data.get("results", [])

def ask_quiz(questions):
    """
    Run an interactive quiz in the terminal. Returns score and count.
    """
    score = 0
    total = len(questions)

    for i, q in enumerate(questions, start=1):
        # decode possible HTML entities
        question_text = html.unescape(q.get("question", ""))
        correct = html.unescape(q.get("correct_answer", ""))
        incorrect = [html.unescape(x) for x in q.get("incorrect_answers", [])]

        options = incorrect + [correct]
        random.shuffle(options)

        # display
        print(f"\nQuestion {i}/{total}: {question_text}")
        for idx, opt in enumerate(options, start=1):
            print(f"  {idx}. {opt}")

        # get valid input
        while True:
            choice = input("Your answer (enter the option number): ").strip()
            if not choice.isdigit():
                print("  Please enter a number (the option index).")
                continue
            choice_num = int(choice)
            if 1 <= choice_num <= len(options):
                break
            print(f"  Enter a number between 1 and {len(options)}.")

        selected = options[choice_num - 1]
        if selected == correct:
            print(" Correct!")
            score += 1
        else:
            print(f"Wrong. Correct answer: {correct}")

    return score, total

def main():
    print("Welcome to the Trivia Quiz!")
    try:
        amt = int(input("How many questions would you like? (1-20, default 5): ") or 5)
    except ValueError:
        amt = 5
    amt = max(1, min(20, amt))

    # Example: General Knowledge category id = 9
    use_category = input("Do you want general knowledge questions? (y/n) [y]: ").strip().lower() or "y"
    category = 9 if use_category == "y" else None

    print("\nFetching questions...")
    questions = fetch_trivia(amount=amt, category=category)
    if not questions:
        print("Could not fetch questions. Try again later.")
        return

    score, total = ask_quiz(questions)
    perc = round((score / total) * 100)
    print(f"\nQuiz finished! Your score: {score}/{total} ({perc}%)")

if __name__ == "__main__":
    main()
