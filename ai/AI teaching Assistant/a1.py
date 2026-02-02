# 1. IMPORT necessary libraries:
#    - streamlit (for UI)
#    - google.genai (for Gemini API interaction)
#    - config (for API key)

# 2. INITIALIZE Gemini API client with API key from config

# 3. DEFINE function generate_response(prompt, temperature=0.3):
#    - Prepare content structure for Gemini API with user's prompt
#    - Configure generation parameters including temperature
#    - Call Gemini API to generate AI response
#    - Return the response text or error message

# 4. DEFINE function setup_ui():
#    - Display the app title and welcome message
#    - Display a text input box for user's question
#    - If user input is provided:
#        - Show user's question
#        - Call generate_response with the user's question
#        - Display AI's answer
#    - Else:
#        - Prompt user to enter a question

# 5. DEFINE function main():
#    - Call setup_ui()

# 6. IF __name__ == "__main__":
#    - Run main()
