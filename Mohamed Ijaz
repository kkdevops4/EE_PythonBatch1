# Student Report Card

students = int(input("\nEnter number of students: "))

for x in range(students):
    name = input("\nEnter student name: ")
    subjects = int(input("\nEnter number of subjects: "))
    marks = []

    for y in range(subjects):
        mark = int(input(f"Enter marks of subject {y+1}: "))
        marks.append(mark)


    average = sum(marks) / len(marks)


    if int(average) >= 90:
      grade = "o"
    elif average >= 80:
      grade = "A+"
    elif average >= 75:
      grade = "A"
    elif average >= 65:
      grade = "B+"
    elif average >= 60:
      grade = "B"
    elif average >= 50:
      grade = "C"
    else:
      grade = "FAIL"



    print("\n----- Report Card -----")
    print("Name: ", name)
    print("Marks: ", marks)
    print("Average: ", average)
    print("Grade: ", grade)
    print("-----------------------")

