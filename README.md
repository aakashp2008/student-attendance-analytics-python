# 🎓 Student Attendance Analytics System

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-blue.svg">
<img src="https://img.shields.io/badge/JSON-Data%20Storage-orange.svg">
<img src="https://img.shields.io/badge/CSV-Reports-green.svg">
<img src="https://img.shields.io/badge/Analytics-Attendance-purple.svg">
<img src="https://img.shields.io/badge/CLI-Application-black.svg">
<img src="https://img.shields.io/badge/Status-Completed-success.svg">
<img src="https://img.shields.io/badge/License-Educational-yellow.svg">

</p>

<p align="center">
  <b>📊 A Python-based system for managing, analyzing, and monitoring student attendance.</b>
</p>

<p align="center">
  <img src="demo.gif" alt="Student Attendance Analytics Demo" width="800">
</p>

## 📖 Overview

The **Student Attendance Analytics System** is a professional Python-based application designed to manage, analyze, and monitor student attendance records.

The system allows users to add students, record attendance, calculate attendance percentages, identify attendance shortages, search student records, update attendance, generate analytics, and export detailed CSV reports.

This project demonstrates practical implementation of **Python programming, data management, file handling, analytics, JSON storage, CSV reporting, CRUD operations, and command-line application development**.

---

## ✨ Features

- 👨‍🎓 Student Management
- 📅 Attendance Recording
- 📊 Attendance Percentage Calculation
- ⚠️ Attendance Shortage Detection
- 🔍 Student Search
- ✏️ Attendance Update
- 🗑️ Student Deletion
- 📈 Attendance Analytics
- 🏆 Highest Attendance Identification
- 📉 Lowest Attendance Identification
- 📄 CSV Report Generation
- 💾 JSON Data Storage
- 🖥️ Command-Line Interface
- ✅ Attendance Eligibility Checking

---

## 🏆 Attendance Evaluation

The system evaluates student attendance based on the attendance percentage.

### Attendance Status

| Attendance | Status |
| ---------- | ------ |
| 75% or above | 🟢 Eligible |
| Below 75% | 🔴 Shortage |

The system automatically calculates:

```text
Attendance Percentage =
(Present Classes / Total Classes) × 100
```

---

## 📊 Attendance Analytics

The application provides detailed attendance analytics including:

- Total Students
- Average Attendance
- Eligible Students
- Shortage Students
- Highest Attendance
- Lowest Attendance

Example:

```text
============================================================
ATTENDANCE ANALYTICS
============================================================

Total Students       : 10
Average Attendance   : 82.50%
Eligible Students    : 8
Shortage Students    : 2

Highest Attendance   : Student Name (96.00%)
Lowest Attendance    : Student Name (58.00%)
```

---

## 💡 Smart Attendance Monitoring

The system automatically analyzes attendance records and identifies students whose attendance is below the required percentage.

Example:

```text
============================================================
ATTENDANCE SHORTAGE REPORT
============================================================

ID: STU003
Name: Student Name
Attendance: 62.50%
Status: SHORTAGE
```

This helps identify students who may need to improve their attendance.

---

## 🛠️ Technologies Used

- Python 3
- JSON
- CSV
- Datetime
- File Handling
- Lists
- Dictionaries
- Functions
- Exception Handling
- Data Processing
- Command-Line Interface

---

## 📂 Project Structure

```text
student-attendance-analytics-python/
│
├── student_attendance_analytics.py
├── attendance_data.json
├── attendance_report.csv
└── README.md
```

The `attendance_data.json` and `attendance_report.csv` files are generated automatically when the corresponding features are used.

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/aakashp2008/student-attendance-analytics-python.git
```

### Navigate to the Project

```bash
cd student-attendance-analytics-python
```

### Run the Program

```bash
python student_attendance_analytics.py
```

No external Python packages are required.

### Programiz

The project uses only Python's standard library, so it can also be executed using the **Programiz Python Online Compiler** without installing external packages.

---

## 🖥️ Main Menu

```text
============================================================
       STUDENT ATTENDANCE ANALYTICS SYSTEM
============================================================

1. Add Student
2. Record Attendance
3. View All Students
4. Search Student
5. Update Attendance
6. Attendance Shortage Report
7. Attendance Analytics
8. Export CSV Report
9. Delete Student
10. Exit
```

---

## 📋 Example

### Add Student

```text
============================================================
ADD STUDENT
============================================================

Enter Student ID: STU001
Enter Student Name: Student Name
Enter Department: Information Technology
Enter Year: 2

Student added successfully!
```

### Record Attendance

```text
============================================================
RECORD ATTENDANCE
============================================================

Enter Student ID: STU001

Student: Student Name

Enter number of classes conducted: 40
Enter number of classes attended: 35

Attendance recorded successfully!

------------------------------------------------------------
ATTENDANCE DETAILS
------------------------------------------------------------

Student ID       : STU001
Student Name     : Student Name
Department       : Information Technology
Total Classes    : 40
Present          : 35
Absent           : 5
Attendance       : 87.50%
Status           : ELIGIBLE
```

---

## 📄 Reports

The application can generate a detailed CSV attendance report containing:

- Student ID
- Student Name
- Department
- Year
- Total Classes
- Present Classes
- Absent Classes
- Attendance Percentage
- Attendance Status

Generated file:

```text
attendance_report.csv
```

The report can be opened using spreadsheet applications such as Microsoft Excel or other compatible software.

---

## 💾 Data Storage

Student attendance information is stored locally using JSON.

Generated file:

```text
attendance_data.json
```

The JSON file stores:

- Student ID
- Student Name
- Department
- Year
- Total Classes
- Present Classes
- Absent Classes
- Attendance Percentage
- Record Creation Date

This makes the application lightweight and easy to run without requiring a database server.

---

## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Python Programming
- Data Management
- Attendance Analysis
- File Handling
- JSON Data Storage
- CSV Report Generation
- Data Structures
- CRUD Operations
- Input Validation
- Functions
- Data Processing
- Conditional Statements
- Exception Handling
- Command-Line Application Development
- Problem-Solving Skills

---

## 🚀 Future Enhancements

- 🌐 Web-Based Attendance System
- 🖥️ Graphical User Interface using Tkinter
- 📱 Mobile Application
- 🗄️ MySQL / SQLite Database
- 📊 Interactive Attendance Charts
- 📈 Monthly Attendance Reports
- 📅 Subject-Wise Attendance Tracking
- 👨‍🏫 Faculty Login
- 👨‍🎓 Student Login
- 🔔 Attendance Shortage Notifications
- 📧 Email Notifications
- 🏆 Attendance Ranking System
- 📄 PDF Report Generation
- ☁️ Cloud Data Storage
- 🔐 User Authentication

---

## 🌟 Project Purpose

Maintaining student attendance manually can be time-consuming and difficult to analyze.

The **Student Attendance Analytics System** provides a simple solution for recording attendance, calculating attendance percentages, identifying attendance shortages, analyzing overall attendance performance, and generating reports.

The project can be extended into a complete **college attendance management and analytics platform**.

---

## 👨‍💻 About

The **Student Attendance Analytics System** was developed as a Python project to demonstrate practical data management, attendance analysis, file handling, and reporting concepts.

The application combines **student management, attendance recording, percentage calculation, shortage detection, analytics, JSON storage, and CSV reporting** into one professional command-line system.

---

## ⭐ Support

If you find this project useful, please consider giving the repository a **⭐ Star** on GitHub.

---

## 📄 License

This project is developed for educational and learning purposes.
