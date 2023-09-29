"""DEFAULT VARIABLES"""
passed = 0
failed = 0
records = [["Name", "Quiz 1", "Quiz 2", "Quiz 3", "CP", "Final Exam", "Grade", "Status"]]

"""FOR ASKING INPUTS"""
while True:
    name = input("Name of Student: ")
    quiz1 = float(input("Quiz 1 (100): "))
    quiz2 = float(input("Quiz 2 (100): "))
    quiz3 = float(input("Quiz 3 (100): "))
    classP = float(input("Class Participation (100): "))
    finalExam = float(input("Final Exam (100): "))

    qTotal = (quiz1 + quiz2 + quiz3)/3
    fGrade = (qTotal * .4) + (classP * .2) + (finalExam * .4)

    if fGrade > 75:
        status = "Passed"
    else:
        status = "Failed"

    grade = f"{fGrade:.2f}"

    studentRecord = [name, quiz1, quiz2, quiz3, classP, finalExam, grade, status]

    records.append(studentRecord)

    anotherRecord = input("Do you want to enter a new student record (Yes or No): ")

    if anotherRecord.lower() == "yes":
        continue
    elif anotherRecord.lower() == "no":
        break
    else:
        print("Invalid answer.")

"""FOR DISPLAYING"""
print("=======================================================================================")
sr = "| {0:^83} |"
print(sr.format("STUDENT RECORDS"))
print("=======================================================================================")

for column in range(len(records)):
    display = "| {0:^7} | {1:^7} | {2:^7} | {3:^7} | {4:^7} | {5:^10} | {6:^7} | {7:^9} |"
    print(display.format((records[column][0]), (records[column][1]), (records[column][2]), (records[column][3]), (records[column][4]), (records[column][5]), (records[column][6]), (records[column][7])))

for column in range(len(records)):
    if records[column][7].lower() == "passed":
        passed = passed + 1
        continue
    elif records[column][7].lower() == "failed":
        failed = failed + 1
        continue
    else:
        continue

print("=======================================================================================")
print(f"There are {passed} student/s who passed the Midterm Period.")
print(f"There are {failed} student/s who failed the Midterm Period.")
print("=======================================================================================")