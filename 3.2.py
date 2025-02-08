# 3.2
def activity_3_2():
    # Get user input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    full_name = f"{first_name} {last_name}"
    
    print(f"Full Name: {full_name}")
    print(f"Full Name (Upper Case): {full_name.upper()}")
    print(f"Full Name (Lower Case): {full_name.lower()}")
    print(f"Length of Full Name: {len(full_name)}")