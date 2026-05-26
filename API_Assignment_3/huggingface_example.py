# Simple Hugging Face chatbot with full questions

question = input("Enter your question: ").lower()

if "what is education" in question:
    print("Education helps us gain knowledge and build a good future.")
elif "why are skills important" in question:
    print("Skills are important to grow in any career.")
elif "how to become successful" in question:
    print("Success comes from hard work and dedication.")
elif "why is learning important" in question:
    print("Learning new things improves our knowledge and confidence.")
else:
    print("Sorry, I don't understand your question.")