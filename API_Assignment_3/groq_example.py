# Simple Groq program

question = input("Ask something: ").lower()

if "ai" in question:
    print("AI means machines can think like humans.")
elif "python" in question:
    print("Python is an easy programming language.")
elif "hello" in question:
    print("Hello! How can I help you?")
else:
    print("Sorry, I don't understand your question.")