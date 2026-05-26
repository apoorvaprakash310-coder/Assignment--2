# Simple text analysis program
# For CampusPe assignment

def count_words(text):
    return len(text.split())

def count_vowels(text):
    v = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in v:
            count += 1
    return count

def count_consonants(text):
    v = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in v:
            count += 1
    return count

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    clean = ""
    for ch in text:
        if ch.isalnum():
            clean += ch.lower()
    return clean == clean[::-1]

def remove_vowels(text):
    v = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in v:
            result += ch
    return result

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq

def longest_word(text):
    words = text.split()
    if len(words) == 0:
        return ""
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    lw = longest_word(text)
    if lw != "":
        print("Longest word:", lw, "(", len(lw), "letters )")

    print("Word Frequency:")
    freq = word_frequency(text)
    for k in freq:
        print(k, ":", freq[k])

text = input("Enter text: ")
analyze_text(text)