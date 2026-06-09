 
questions = [
    {
        "question": "1. What is the SI unit of pressure?",
        "options": ["A. Joule", "B. Pascal", "C. Watt", "D. Newton"],
        "answer": "B"
    },
 
    {
        "question": "2. Which law states energy cannot be created or destroyed?",
        "options": [
            "A. Zeroth Law",
            "B. Second Law",
            "C. First Law",
            "D. Third Law"
        ],
        "answer": "C"
    },
 
    {
        "question": "3. Which thermodynamic process occurs at constant temperature?",
        "options": [
            "A. Isobaric",
            "B. Isochoric",
            "C. Adiabatic",
            "D. Isothermal"
        ],
        "answer": "D"
    },
 
    {
        "question": "4. What is the efficiency of a Carnot engine always dependent on?",
        "options": [
            "A. Pressure",
            "B. Volume",
            "C. Temperature",
            "D. Mass"
        ],
        "answer": "C"
    },
 
    {
        "question": "5. Which property is intensive?",
        "options": [
            "A. Mass",
            "B. Volume",
            "C. Density",
            "D. Energy"
        ],
        "answer": "C"
    },
   
 
    {
        "question": "6. What does ADAS stand for?",
        "options": [
            "A. Automatic Driving Assistance System",
            "B. Advanced Driver Assistance Systems",
            "C. Advanced Driving Automatic System",
            "D. Automated Driver Alert System"
        ],
        "answer": "B"
    },
 
    {
        "question": "7. Which sensor is commonly used in ADAS for distance measurement?",
        "options": [
            "A. Thermocouple",
            "B. Tachometer",
            "C. LiDAR",
            "D. Vernier Caliper"
        ],
        "answer": "C"
    },
 
    {
        "question": "8. Which ADAS feature helps maintain a safe distance from the vehicle ahead?",
        "options": [
            "A. Cruise Control",
            "B. Adaptive Cruise Control",
            "C. Parking Sensor",
            "D. ABS"
        ],
        "answer": "B"
    }
]
 
score = 0
streak = 0
correct_answers = 0
 
results = []
 
print("--Quiz Test--")
 
 
for q in questions:
    print("\n" + q["question"])
    
    for option in q["options"]:
        print(option)
 
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
 
    if user_answer == q["answer"]:
        print("Correct!")
 
        correct_answers += 1
        streak += 1
        score += 10
 
        if streak >= 2:
            bonus = 5
            score += bonus
            print("Streak Bonus +5 points!")
 
        results.append("Correct")
 
    else:
        print("Wrong!")
        print("Correct Answer is:", q["answer"])
 
        streak = 0
 
        results.append("Wrong")
 
print("--SCORECARD--")
 
print("Total Questions :", len(questions))
print("Correct Answers :", correct_answers)
print("Wrong Answers   :", len(questions) - correct_answers)
print("Final Score     :", score)
 
percentage = (correct_answers / len(questions)) * 100
print("Percentage: ", percentage, "%")
 
if percentage >= 80:
    print("Performance     : Excellent")
elif percentage >= 60:
    print("Performance     : Good")
elif percentage >= 40:
    print("Performance     : Average")
else:
    print("Performance     : Needs Improvement\n Come with your Parents in next PTM.")
 
 
print("\nQuestion Wise Report:")
 
for i in range(len(results)):
    print("Question", i + 1, ":", results[i])
 
print("Thanks for Participating!")  
    