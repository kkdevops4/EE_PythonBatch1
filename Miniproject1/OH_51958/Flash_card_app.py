def flashcard():
    quiz = [
        ("What is the keyword for Multiple Inheritance in Kotlin? ", "interface"),
        ("Write the correct answer for 5 + 7.0: ", "12.0"),
        ("What keyword is used to stop a loop? ", "break"),
        ("Which data type is used to store multiple items? ","list"),
        ("What data type is immutable: list or tuple? ","tuple")
    ]

    for question, answer in quiz:
        while True:
            
            user_answer = input(question).lower()

            if user_answer == answer:
                print("Your answer is correct \n")
                break
            else:
                print("Your answer is incorrect , try again.\n")

    print("Congratulations! You have entered all correct answers...")

flashcard()