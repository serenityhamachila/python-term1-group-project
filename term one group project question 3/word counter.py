# ==========================================
# Term 1 Group Project
# Question 3 — Word Counter
# ==========================================

def word_counter():
    # Ask user for a sentence
    sentence = input("Enter a sentence: ").strip()

    # Check if sentence is empty
    if sentence == "":
        print("Invalid input. Please enter a sentence.")
        return

    # Split sentence into words
    words = sentence.split()

    # Count words
    word_count = len(words)

    # Count characters (excluding spaces)
    char_count = len(sentence.replace(" ", ""))

    # Find longest word
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    # Print results
    print("\n--- Results ---")
    print("Number of words:", word_count)
    print("Number of characters (no spaces):", char_count)
    print("Longest word:", longest_word)


# Run the program
if __name__ == "__main__":
    word_counter()
    input("\nPress Enter to exit...")
