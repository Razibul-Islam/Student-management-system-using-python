import csv
import utilitis


# Function to create a new account
def create_account():
    # Get user input for account information
    name = input("Enter your name: ")
    roll = input("Enter your roll number: ")
    semester = input("Enter your semester: ")
    department = input("Enter your department: ")
    college = input("Enter your college: ")
    password = input("Enter your password: ")
    initialMoney = 1000

    # If There is not provide any Information Account will be not created
    if not all([name, roll, semester, department, college, password]):
        print("Please provide all information to create an account & Try Again")
        return

        # if Roll and semester and Collage is same then return
    with open('accounts.csv', 'r') as file:
        for line in file:
            account_info = line.strip().split(',')
            if account_info[1] == roll and account_info[2] == semester and account_info[4] == college.upper() and \
                    account_info[3] == department.capitalize():
                print("An account with the same details already exists!")
                return

    # Save the account information to a CSV file
    with open('accounts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            [name, roll, semester, department.capitalize(), college.upper(), str(initialMoney), password])
    print(f"Welcome {name}. Account created successfully. Your Initial Money is 1000TK")
    utilitis.menuPrint()


def login():
    # Get user input for login credentials
    roll = input("Enter your Roll: ")
    password = input("Enter your password: ")
    semester = input("Enter Your Semester: ")

    # Check if the input credentials match any account in the file
    with open("accounts.csv", "r") as file:
        for line in file:
            account_info = line.strip().split(",")
            if account_info[1] == roll and account_info[6] == password and account_info[2] == semester:
                print("Login successful!")
                print(f"Welcome, {account_info[0]}")
                utilitis.menuPrint()
                return
    print("Incorrect Roll number or password. Please try again.")
    main()


def main():
    while True:
        print("1. Create Account")
        print("2. Login")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
            break
        elif choice == "2":
            login()
            break
        else:
            print("Invalid choice. Please try again.")
