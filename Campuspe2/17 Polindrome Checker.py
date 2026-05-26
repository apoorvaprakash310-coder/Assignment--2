# This program helps you check whether your input is a palindrome
text = input("Please enter a word or a number: ")

clean_text = text.lower()
reversed_text = clean_text[::-1]

# This part shows the original and reversed values and gives the result
print("Original:", text)
print("Reversed:", text[::-1])

if clean_text == reversed_text:
    print("Result: It is a PALINDROME")
else:
    print("Result: It is NOT a palindrome")