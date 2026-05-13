no_std = int(input("Enter no of students: "))

for j in range(no_std):

    name = input("Enter student Full name: ")
    sub = int(input("Enter total no. of subjects: "))

    marks_list = []
    subject_names = []

    for i in range(sub):

        subject = input(f"Enter subject {i+1} name: ")
        marks = int(input(f"Enter marks of {subject}: "))

        subject_names.append(subject)
        marks_list.append(marks)

    # Calculating Sum
    total = 0
    for m in marks_list:
        total += m

    # Calculating Avg
    avg = total / sub

    # Calculating Percentage
    percentage = round((total / (sub * 100)) * 100, 2) 

    # Grade
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 45:
        grade = "D"
    else:
        grade = "E"

    # Finding failed subjects
    failed_subjects = []

    for i in range(sub):
        if marks_list[i] < 18:
            failed_subjects.append(subject_names[i])

    # Pass OR Fail
    if avg <= 35 or len(failed_subjects) > 0:
        status = "Fail"
    else:
        status = "Pass"

    # Report Card
    print("--------------- Report Card ---------------------")
    print("Name:", name)
    print("Marks:", marks_list)
    print("Total:", total)
    print("Average:", avg)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    print("Status:", status)

    # Printing failed subjects
    if len(failed_subjects) > 0:
        print("Failed in subjects:", failed_subjects)

    print("------------- Thank You!!----------------------")