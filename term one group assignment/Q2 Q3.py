# ==========================================
# Term 1 Group Project
# Question 2 - Grade System
# Question 3 - Word Counter
# ==========================================


# -------------------------------
# QUESTION 2 — GRADE SYSTEM
# -------------------------------
def grade_system():
    marks = []
    print("\nEnter 5 marks (0 - 100):")

    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter mark {i+1}: "))
                
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Mark must be between 0 and 100.")
            
            except ValueError:
                print("Invalid input. Please enter a number.")

    average = sum(marks) / 5

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\nAverage:", round(average, 2))
    print("Grade:", grade)


# -------------------------------
# QUESTION 3 — WORD COUNTER
# -------------------------------
def word_counter():
    sentence = input("\nEnter a sentence: ").strip()

    if sentence == "":
        print("Invalid input. Please enter a sentence.")
        return

    words = sentence.split()
    word_count = len(words)

    char_count = len(sentence.replace(" ", ""))

    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    print("\nNumber of words:", word_count)
    print("Number of characters (no spaces):", char_count)
    print("Longest word:", longest_word)


# -------------------------------
# SIMPLE MENU (For Testing)
# -------------------------------
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 → Grade System")
        print("2 → Word Counter")
        print("0 → Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            grade_system()
        elif choice == "2":
            word_counter()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Run program
menu()
