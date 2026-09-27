# Study-Buddy – Exam Readiness Analyzer

## Project Overview

**Study Buddy – Exam Readiness Analyzer** is a command-line Python application designed to help students track their academic readiness for exams.

The program allows a student to enter subject-wise **attendance percentage, internal marks, and planned weekly study hours**. It then checks how many readiness conditions are satisfied and displays a simple exam-readiness status for each subject.

The application also saves the entered subject data in a text file so that the information can be loaded again when the program is started.

---

## Objectives

The main objectives of this project are:

- To store subject-wise academic information.
- To track attendance, internal marks, and planned study hours.
- To check a student's exam readiness using simple conditions.
- To provide an easy-to-understand readiness status.
- To save data between different program sessions.
- To demonstrate fundamental Python programming concepts through a practical application.

---

## Features

### 1. Add Subject

The user can enter:

- Subject name
- Attendance percentage
- Internal marks out of 100
- Study hours planned for the week

If the subject already exists, the program gives the option to update its information.

### 2. View Subjects

The program displays all saved subjects together with:

- Attendance
- Internal marks
- Planned weekly study hours

### 3. Check Exam Readiness

The program evaluates every subject using three conditions:

| Condition | Requirement |
|---|---:|
| Attendance | 75% or above |
| Internal Marks | 45 or above |
| Weekly Study Hours | 4 hours or above |

Each satisfied condition contributes **1 point**, giving a maximum of **3 points**.

The program then displays a readiness status based on the number of conditions satisfied.

### 4. Save and Load Data

Subject information is stored in a file named `subjects.txt`.

When the program starts, it automatically attempts to load previously saved data. When the user chooses **Save and exit**, the current subject information is written to the file.

This allows the program to maintain data across different sessions.

---

## Readiness Logic

The readiness calculation is based on three simple rules.

### Condition 1 – Attendance

If:

```text
Attendance >= 75%
```

the student receives 1 readiness point.

### Condition 2 – Internal Marks

If:

```text
Internal Marks >= 45
```

the student receives 1 readiness point.

### Condition 3 – Study Hours

If:

```text
Weekly Study Hours >= 4
```

the student receives 1 readiness point.

### Final Status

| Conditions Met | Status |
|---:|---|
| 3 / 3 | Ready for exam! |
| 2 / 3 | Good for exam |
| 1 / 3 | Not good, need more efforts |
| 0 / 3 | Unacceptable, you cant pass this |

The program displays the result separately for every subject.

> **Note:** These are simple rule-based readiness conditions implemented in the current version of the project. They are not machine-learning predictions or official academic grading rules.

---

## Technologies Used

- **Python 3**
- Python built-in functions and data structures
- Text file handling
- Command-line / terminal interface

No external Python libraries are required for the current version.

---

## Python Concepts Used

This project demonstrates several fundamental Python concepts:

| Python Concept | Use in Project |
|---|---|
| Variables | Store subject information and calculations |
| Lists | Store multiple subjects |
| Nested lists | Store subject details together |
| Functions | Organize program operations |
| `if / elif / else` | Implement readiness rules and menu choices |
| `for` loops | Process subjects and load saved data |
| `while` loop | Keep the menu running |
| User input | Collect subject information |
| Type conversion | Convert input into `float` values |
| String methods | Compare subject names and process file lines |
| File handling | Save and load subject data |
| Exception handling | Handle a missing data file |
| Basic calculations | Count satisfied readiness conditions |

---

## Project Structure

```text
study-buddy/
│
├── studybuddy.py
├── subjects.txt
└── README.md
```

### File Description

**`studybuddy.py`**  
Contains the complete Python program, including data loading, data saving, subject management, readiness checking, and the main menu.

**`subjects.txt`**  
Stores saved subject information. Each line contains:

```text
Subject Name,Attendance,Marks,Study Hours
```

**`README.md`**  
Contains project information, setup instructions, features, logic, and usage details.

---

## Requirements

### Software Requirements

- Python 3.x
- Terminal / Command Prompt
- Git (optional, for GitHub submission)

### Libraries

The current project uses only Python's built-in features.

**No external packages are required.**

Therefore, a `requirements.txt` file is not necessary for the current version.

---

## How to Set Up the Project

### Step 1 – Install Python

Install Python 3.x on your computer.

Check whether Python is installed:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

---

### Step 2 – Get the Project

If the project is available on GitHub, clone the repository:

```bash
git clone https://github.com/{github-username}/{repo-name}.git
```

Move into the project folder:

```bash
cd {repo-name}
```

Replace `{github-username}` and `{repo-name}` with the actual GitHub username and repository name.

---

### Step 3 – Run the Program

Run:

```bash
python studybuddy.py
```

If your system uses `python3`:

```bash
python3 studybuddy.py
```

The program runs completely through the terminal and does not require a graphical interface.

---

## How to Use the Program

After starting the program, the following menu appears:

```text
----- Study Buddy: Exam Readiness Checker -----
1. Add subject
2. View subjects
3. Check exam readiness
4. Save and exit
Enter choice:
```

### Option 1 – Add Subject

Enter:

```text
Enter subject name: Python
Enter attendance %: 85
Enter internal marks (out of 100): 72
Enter study hours planned this week: 5
```

The subject is then stored in memory.

If the subject already exists, the program asks whether you want to update it.

---

### Option 2 – View Subjects

The program displays the stored subjects in a simple table:

```text
Name            Attendance      Marks   Hours
Python          85.0            72.0    5.0
Mathematics     78.0            61.0    4.0
English         92.0            80.0    6.0
```

---

### Option 3 – Check Exam Readiness

The program checks the three readiness conditions.

Example:

```text
Subject Readiness:

Python -> Ready for exam! ( 3 /3 conditions met )
Mathematics -> Good for exam ( 2 /3 conditions met )
English -> Ready for exam! ( 3 /3 conditions met )
```

---

### Option 4 – Save and Exit

Selecting option `4` saves the current subject data to `subjects.txt` and exits the program.

```text
Data saved. Bye!
```

The saved information can be loaded automatically the next time the program is started.

---

## Data Storage Format

The project uses a simple text file instead of an external database.

Example `subjects.txt`:

```text
Python,85,72,5
Mathematics,78,61,4
English,92,80,6
```

The four values represent:

```text
Subject Name, Attendance, Internal Marks, Weekly Study Hours
```

When the program starts, these values are read from the file and converted into numerical values where required.

---

## Error Handling

The current program includes handling for a missing `subjects.txt` file.

If the file does not exist when the program starts, the program simply begins with an empty subject list instead of terminating.

The program also checks whether a subject already exists before adding it, allowing the user to update the existing information.

---

## Design Approach

The project follows a simple function-based design.

### Main Program Flow

```text
Start
  |
  v
Load saved subject data
  |
  v
Display menu
  |
  +----> Add Subject
  |          |
  |          v
  |     Store subject data
  |
  +----> View Subjects
  |          |
  |          v
  |     Display saved data
  |
  +----> Check Exam Readiness
  |          |
  |          v
  |     Check 3 conditions
  |          |
  |          v
  |     Display readiness status
  |
  +----> Save and Exit
             |
             v
       Save to subjects.txt
             |
             v
            End
```

---

## Limitations of the Current Version

The current version is intentionally based on simple Python concepts.

Some possible limitations are:

- It does not use a graphical user interface.
- It does not use a database.
- Input validation for invalid numerical ranges can be improved.
- The readiness rules are fixed in the program.
- It does not calculate an actual final examination grade.
- It does not use machine learning.
- It does not automatically generate a detailed weekly study timetable.
- The data is stored in a simple text file.

---

## Future Scope

The project can be extended in future versions by adding:

- Input validation for attendance, marks, and study hours.
- A more detailed performance prediction system.
- Subject-wise risk levels such as Low, Medium, and High.
- Automatic weekly study-hour recommendations.
- CSV or JSON-based data storage.
- A graphical user interface.
- Charts showing subject performance.
- More detailed academic analytics.
- A machine-learning model if ML concepts are included in the course.
- Separate modules such as `analyzer.py`, `recommender.py`, and `storage.py` as the project grows.

---

## Academic Relevance

The project is designed around fundamental Python programming concepts and applies them to a practical student-focused problem.

It demonstrates:

**Input → Processing → Decision Making → Output → File Storage**

The project therefore provides a practical example of using Python programming concepts in a command-line application.

---

## Project Execution Checklist

Before submission, verify:

- [ ] The GitHub repository is **Public**.
- [ ] `README.md` is present in the repository root.
- [ ] The Python program runs from the terminal.
- [ ] `subjects.txt` can be created/updated by the program.
- [ ] The repository root URL is submitted, not a `/tree/` or `/blob/` URL.
- [ ] The project report is submitted separately according to the VITyarthi instructions.
- [ ] The final repository is tested on a fresh Python environment.

## Conclusion

**Study Buddy – Exam Readiness Analyzer** is a simple command-line Python project that helps students monitor their subject-wise exam readiness using attendance, internal marks, and planned study hours.

The project combines fundamental Python concepts such as functions, lists, loops, conditional statements, user input, string processing, and file handling into one practical application.

The design can also be expanded in future versions into a more advanced academic performance and study-planning system.
