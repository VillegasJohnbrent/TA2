# 3.3
def activity_3_3():
    # Get user input
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    age = input("Enter age: ")
    contact = input("Enter contact number: ")
    course = input("Enter course: ")

    student_info = (
        f"Last Name: {last_name}\n"
        f"First Name: {first_name}\n"
        f"Age: {age}\n"
        f"Contact Number: {contact}\n"
        f"Course: {course}"
    )
    
    # Write to file
    with open("students.txt", "a") as file:
        file.write(student_info + "\n\n")
    
    print("Student information has been saved to 'students.txt'.")