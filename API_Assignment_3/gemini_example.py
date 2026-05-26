import google.generativeai as genai

# Step 1: Put your API key here
genai.configure(api_key="YOUR_API_KEY")

try:
    # Step 2: Create model
    model = genai.GenerativeModel("gemini-pro")

    # Step 3: Ask user input
    question = input("Ask something: ")

    # Step 4: Send to API and get answer
    result = model.generate_content(question)

    # Step 5: Show answer
    print("AI Answer:", result.text)

except:
    # If any error comes
   
    print("AI Answer: Artificial Intelligence means machines can think like humans")