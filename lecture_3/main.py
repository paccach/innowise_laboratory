def main():
    def new_student():
        student_name = input("Enter student name: ").strip()
        if student_name:
            if not any(s["name"].lower() == student_name.lower() for s in students):
                #  if student_name not in [student["name"]
                #   for student in students]:
                student = {"name": student_name, "grades": []}
                students.append(student)
            else:
                print("This student already exists.")
        else:
            print("Student name cannot be empty.")

    def add_grade():
        student_name = input("Enter a student name: ").strip()
        student = None
        for i in students:
            if i["name"].lower() == student_name.lower():
                student = i
                break
        if student:
            while True:
                grade = input("Enter a grade (or 'done' to finish): ").strip()
                if grade == "done":
                    break
                try:
                    if 0 <= int(grade) <= 100:
                        student['grades'].append(int(grade))
                    else:
                        print("Invalid input. Please enter a number between 0 and 100.")
                except (ValueError, TypeError):
                    print("Invalid input. Please enter a number.")
        else:
            print("This student is not in the system")

    def show_report():
        if not students:
            print("No students yet.")
            return
        average_grades = []
        print("--- Student Report ---")
        for student in students:
            try:
                average = sum(student["grades"]) / len(student["grades"])
                average_grades.append(average)
                print(f"{student['name']}'s average grade is {average:.1f}")
            except ZeroDivisionError:
                print(f"{student['name']}'s average grade is N/A")
        print("-" * 26)
        try:
            max_average = max(average_grades)
            min_average = min(average_grades)
            overall_average = sum(average_grades) / len(average_grades)
            print(f"Max Average: {max_average:.1f}")
            print(f"Min Average: {min_average:.1f}")
            print(f"Overall Average: {overall_average:.1f}")
        except (TypeError, ValueError):
            print("There are no grades at all.")

    def find_top():
        try:
            top_student = max(students, key=lambda student: sum(student["grades"]) / len(student["grades"]) if student["grades"] else 0, default=None)
            if top_student:
                name = top_student["name"]
                average = sum(top_student["grades"]) / len(top_student["grades"])
                print(f"The student with the highest average is {name} with a grade of {average:.1f}.")
            else:
                print("There are no grades or students at all.")
        except ZeroDivisionError:
            print("There are no grades or students at all.")

    students = []

    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                new_student()
            elif choice == 2:
                add_grade()
            elif choice == 3:
                show_report()
            elif choice == 4:
                find_top()
            elif choice == 5:
                print("Exiting program.")
                return
            else:
                print("An error occurred. Please enter a number between 1 and 5.")
        except ValueError:
            print("An error occurred. Please enter a number between 1 and 5.")
        except KeyboardInterrupt:
            print("Exiting program.")
            return


if __name__ == "__main__":
    main()
