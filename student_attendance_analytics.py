import json
import csv
from datetime import datetime

DATA_FILE = "attendance_data.json"
REPORT_FILE = "attendance_report.csv"


# ============================================================
# DATA HANDLING
# ============================================================

def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_data(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


# ============================================================
# INPUT VALIDATION
# ============================================================

def get_integer(message, minimum=0):
    while True:
        try:
            value = int(input(message))

            if value >= minimum:
                return value

            print("Please enter a valid value.")

        except ValueError:
            print("Please enter a number.")


def get_percentage(message):
    while True:
        try:
            value = float(input(message))

            if 0 <= value <= 100:
                return value

            print("Enter a percentage between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


# ============================================================
# ADD STUDENT
# ============================================================

def add_student(students):

    print("\n" + "=" * 60)
    print("ADD STUDENT")
    print("=" * 60)

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student["id"].lower() == student_id.lower():
            print("Student ID already exists.")
            return

    name = input("Enter Student Name: ").strip()
    department = input("Enter Department: ").strip()
    year = get_integer("Enter Year: ", 1)

    student = {
        "id": student_id,
        "name": name,
        "department": department,
        "year": year,
        "total_classes": 0,
        "present": 0,
        "absent": 0,
        "attendance_percentage": 0.0,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    students.append(student)
    save_data(students)

    print("\nStudent added successfully!")


# ============================================================
# RECORD ATTENDANCE
# ============================================================

def record_attendance(students):

    print("\n" + "=" * 60)
    print("RECORD ATTENDANCE")
    print("=" * 60)

    student_id = input("Enter Student ID: ").strip()

    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nStudent:", student["name"])

    total = get_integer(
        "Enter number of classes conducted: ",
        1
    )

    present = get_integer(
        "Enter number of classes attended: ",
        0
    )

    if present > total:
        print("Present classes cannot be greater than total classes.")
        return

    absent = total - present

    student["total_classes"] = total
    student["present"] = present
    student["absent"] = absent

    student["attendance_percentage"] = (
        present / total
    ) * 100

    save_data(students)

    print("\nAttendance recorded successfully!")

    display_attendance(student)


# ============================================================
# DISPLAY ATTENDANCE
# ============================================================

def display_attendance(student):

    percentage = student["attendance_percentage"]

    print("\n" + "-" * 60)
    print("ATTENDANCE DETAILS")
    print("-" * 60)

    print("Student ID       :", student["id"])
    print("Student Name     :", student["name"])
    print("Department       :", student["department"])
    print("Total Classes    :", student["total_classes"])
    print("Present          :", student["present"])
    print("Absent           :", student["absent"])
    print(f"Attendance       : {percentage:.2f}%")

    if percentage >= 75:
        print("Status           : ELIGIBLE")
    else:
        print("Status           : SHORTAGE")

    print("-" * 60)


# ============================================================
# FIND STUDENT
# ============================================================

def find_student(students, student_id):

    for student in students:

        if student["id"].lower() == student_id.lower():
            return student

    return None


# ============================================================
# VIEW ALL STUDENTS
# ============================================================

def view_students(students):

    print("\n" + "=" * 60)
    print("ALL STUDENTS")
    print("=" * 60)

    if not students:
        print("No student records found.")
        return

    for student in students:

        print(
            f"\nID: {student['id']}"
        )

        print(
            f"Name: {student['name']}"
        )

        print(
            f"Department: {student['department']}"
        )

        print(
            f"Year: {student['year']}"
        )

        print(
            f"Attendance: "
            f"{student['attendance_percentage']:.2f}%"
        )


# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student(students):

    print("\n" + "=" * 60)
    print("SEARCH STUDENT")
    print("=" * 60)

    keyword = input(
        "Enter Student ID or Name: "
    ).strip().lower()

    if not keyword:
        print("Search value cannot be empty.")
        return

    results = []

    for student in students:

        if (
            keyword in student["id"].lower()
            or keyword in student["name"].lower()
        ):
            results.append(student)

    if not results:
        print("No matching student found.")
        return

    for student in results:
        display_attendance(student)


# ============================================================
# UPDATE ATTENDANCE
# ============================================================

def update_attendance(students):

    print("\n" + "=" * 60)
    print("UPDATE ATTENDANCE")
    print("=" * 60)

    student_id = input("Enter Student ID: ").strip()

    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nCurrent attendance:")
    display_attendance(student)

    total = get_integer(
        "Enter updated total classes: ",
        1
    )

    present = get_integer(
        "Enter updated present classes: ",
        0
    )

    if present > total:
        print("Present classes cannot be greater than total classes.")
        return

    student["total_classes"] = total
    student["present"] = present
    student["absent"] = total - present

    student["attendance_percentage"] = (
        present / total
    ) * 100

    save_data(students)

    print("\nAttendance updated successfully!")


# ============================================================
# ATTENDANCE SHORTAGE
# ============================================================

def attendance_shortage(students):

    print("\n" + "=" * 60)
    print("ATTENDANCE SHORTAGE REPORT")
    print("=" * 60)

    shortage_found = False

    for student in students:

        percentage = student["attendance_percentage"]

        if percentage < 75:

            shortage_found = True

            print(
                f"\nID: {student['id']}"
            )

            print(
                f"Name: {student['name']}"
            )

            print(
                f"Attendance: {percentage:.2f}%"
            )

            print(
                "Status: SHORTAGE"
            )

    if not shortage_found:
        print("\nNo students have attendance shortage.")


# ============================================================
# ANALYTICS
# ============================================================

def analytics(students):

    print("\n" + "=" * 60)
    print("ATTENDANCE ANALYTICS")
    print("=" * 60)

    if not students:
        print("No student records available.")
        return

    total_students = len(students)

    attendance_values = [
        student["attendance_percentage"]
        for student in students
    ]

    average = (
        sum(attendance_values)
        / total_students
    )

    eligible = 0
    shortage = 0

    for student in students:

        if student["attendance_percentage"] >= 75:
            eligible += 1
        else:
            shortage += 1

    highest = max(
        students,
        key=lambda student:
        student["attendance_percentage"]
    )

    lowest = min(
        students,
        key=lambda student:
        student["attendance_percentage"]
    )

    print("Total Students       :", total_students)
    print(f"Average Attendance   : {average:.2f}%")
    print("Eligible Students    :", eligible)
    print("Shortage Students    :", shortage)

    print(
        "\nHighest Attendance   :",
        highest["name"],
        f"({highest['attendance_percentage']:.2f}%)"
    )

    print(
        "Lowest Attendance    :",
        lowest["name"],
        f"({lowest['attendance_percentage']:.2f}%)"
    )


# ============================================================
# EXPORT CSV REPORT
# ============================================================

def export_report(students):

    print("\n" + "=" * 60)
    print("EXPORT ATTENDANCE REPORT")
    print("=" * 60)

    if not students:
        print("No records available.")
        return

    with open(
        REPORT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Student ID",
            "Name",
            "Department",
            "Year",
            "Total Classes",
            "Present",
            "Absent",
            "Attendance Percentage",
            "Status"
        ])

        for student in students:

            percentage = student[
                "attendance_percentage"
            ]

            status = (
                "Eligible"
                if percentage >= 75
                else "Shortage"
            )

            writer.writerow([
                student["id"],
                student["name"],
                student["department"],
                student["year"],
                student["total_classes"],
                student["present"],
                student["absent"],
                f"{percentage:.2f}%",
                status
            ])

    print(
        "\nReport exported successfully!"
    )

    print(
        "File:",
        REPORT_FILE
    )


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student(students):

    print("\n" + "=" * 60)
    print("DELETE STUDENT")
    print("=" * 60)

    student_id = input(
        "Enter Student ID: "
    ).strip()

    student = find_student(
        students,
        student_id
    )

    if student is None:
        print("Student not found.")
        return

    print(
        "\nStudent:",
        student["name"]
    )

    confirmation = input(
        "Delete this student? (yes/no): "
    ).strip().lower()

    if confirmation != "yes":
        print("Deletion cancelled.")
        return

    students.remove(student)

    save_data(students)

    print(
        "\nStudent deleted successfully!"
    )


# ============================================================
# MAIN MENU
# ============================================================

def main():

    students = load_data()

    print("=" * 60)
    print("       STUDENT ATTENDANCE ANALYTICS SYSTEM")
    print("=" * 60)

    while True:

        print("\n" + "=" * 60)
        print("MAIN MENU")
        print("=" * 60)

        print("1. Add Student")
        print("2. Record Attendance")
        print("3. View All Students")
        print("4. Search Student")
        print("5. Update Attendance")
        print("6. Attendance Shortage Report")
        print("7. Attendance Analytics")
        print("8. Export CSV Report")
        print("9. Delete Student")
        print("10. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            record_attendance(students)

        elif choice == "3":
            view_students(students)

        elif choice == "4":
            search_student(students)

        elif choice == "5":
            update_attendance(students)

        elif choice == "6":
            attendance_shortage(students)

        elif choice == "7":
            analytics(students)

        elif choice == "8":
            export_report(students)

        elif choice == "9":
            delete_student(students)

        elif choice == "10":

            print(
                "\nThank you for using "
                "Student Attendance Analytics System."
            )

            print("Goodbye! 👋")
            break

        else:

            print(
                "\nInvalid choice. Please try again."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
