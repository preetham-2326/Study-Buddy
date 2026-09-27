subjects = []
FILENAME = "subjects.txt"

def load_data():
    try:
        file = open(FILENAME, "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            name = parts[0]
            attendance = float(parts[1])
            marks = float(parts[2])
            hours = float(parts[3])
            subjects.append([name, attendance, marks, hours])
        file.close()
    except FileNotFoundError:
        pass

def save_data():
    file = open(FILENAME, "w")
    for s in subjects:
        line = s[0] + "," + str(s[1]) + "," + str(s[2]) + "," + str(s[3]) + "\n"
        file.write(line)
    file.close()

def find_subject_index(name):
    for i in range(len(subjects)):
        if subjects[i][0].lower() == name.lower():
            return i
    return -1

def add_subject():
    name = input("Enter subject name: ")
 
    index = find_subject_index(name)
 
    if index != -1:
        choice = input("This subject is already added. Update it? (y/n): ")
 
        if choice.lower() == "n":
            print("Okay, not updating.\n")
            return
        elif choice.lower() == "y":
            attendance = float(input("Enter attendance %: "))
            marks = float(input("Enter internal marks (out of 100): "))
            hours = float(input("Enter study hours planned this week: "))
            subjects[index] = [name, attendance, marks, hours]
            print("Subject updated.\n")
            return
        else:
            print("Invalid choice, not updating.\n")
            return
 
    attendance = float(input("Enter attendance %: "))
    marks = float(input("Enter internal marks (out of 100): "))
    hours = float(input("Enter study hours planned this week: "))
    subjects.append([name, attendance, marks, hours])
    print("Subject added.\n")

def view_subjects():
    if len(subjects) == 0:
        print("No subjects added yet.\n")
        return
    print("\nName\t\tAttendance\tMarks\tHours")
    for s in subjects:
        print(s[0], "\t", s[1], "\t\t", s[2], "\t", s[3])
    print()

def check_status():
    if len(subjects) == 0:
        print("No subjects added yet.\n")
        return
    print("\nSubject Readiness:\n")
    for s in subjects:
        name = s[0]
        attendance = s[1]
        marks = s[2]
        hours = s[3]

        count = 0

        if attendance >= 75:
            count = count + 1

        if marks >= 45:
            count = count + 1

        if hours >= 4:
            count = count + 1

        if count == 3:
            status = "Ready for exam!"
        elif count == 2:
            status = "Good for exam"
        elif count == 1:
            status = "Not good, need more efforts"
        else:
            status = "Unacceptable, you cant pass this"

        print(name, "->", status, "(", count, "/3 conditions met )")
    print()

#------------main-----------------
load_data()

while True:
    print("----- Study Buddy: Exam Readiness Checker -----")
    print("1. Add subject")
    print("2. View subjects")
    print("3. Check exam readiness")
    print("4. Save and exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_subject()
    elif choice == "2":
        view_subjects()
    elif choice == "3":
        check_status()
    elif choice == "4":
        save_data()
        print("Data saved. Bye!")
        break
    else:
        print("Invalid choice, try again.\n")
