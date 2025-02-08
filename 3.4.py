# 3.4
def activity_3_4():
    print("Reading Student Information:")
    try:
        with open("students.txt", "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("Error: students.txt file not found.")