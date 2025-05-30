"""
A simple utility to count the number of words in a user-provided string.
Handles edge cases like empty input and special characters.
"""

def count_words(text):
    # Split on whitespace, filter out empty strings (handles multiple spaces)
    words = [word for word in text.strip().split() if word]
    return len(words)

if __name__ == "__main__":
    user_input = input("Enter some text: ")
    word_count = count_words(user_input)
    print(f"Input Text: {user_input}")
    print(f"Word Count: {word_count}")