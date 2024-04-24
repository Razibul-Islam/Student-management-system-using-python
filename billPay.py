import datetime
import utilitis

menus = ["Tuition Fee", "Semester Fee", "Canteen Fee", "Main Menu"]


def inputValue():
    roll = input("Enter Your Roll Number: ")
    collage = input("Enter Your College Name: ")
    semester = input("Enter Your Semester: ")
    department = input("Enter your department: ")
    return roll, collage, semester, department


def payBill():
    roll, collage, semester, department = inputValue()

    with open("accounts.csv", "r") as file:
        for line in file:
            account_info = line.strip().split(",")
            if account_info[1] == roll and account_info[4] == collage.upper() and account_info[2] == semester and \
                    account_info[3] == department.capitalize():
                return roll, collage, semester, department


def tuitionFee():
    update_Contents = []
    roll, collage, semester, department = payBill()
    amount = input("Enter Tuition Fee amount: ")
    intAmount = int(amount)
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("billInformation.csv", "a") as file:
        file.write(f"{roll},{collage},{semester},{department},{amount},{current_datetime},Tuition Fee\n")

    # Add a confirmation message
    with open("accounts.csv", "r") as file2:
        for line in file2:
            account_info = line.strip().split(',')
            if account_info[1] == roll and account_info[4] == collage.upper() and account_info[2] == semester and \
                    account_info[3] == department.capitalize():
                old_Balance = int(account_info[5])
                account_info[5] = str(old_Balance - intAmount)
                print(f"{account_info[0]}, {amount}TK added your Tuition Fee.")
            update_Contents.append(",".join(account_info))
    with open("accounts.csv", 'w') as file:
        for account_line in update_Contents:
            file.write(account_line + "\n")
    utilitis.menuPrint()


def semesterFee():
    update_Contents = []
    roll, collage, semester, department = payBill()
    amount = input("Enter Semester Fee amount: ")
    intAmount = int(amount)
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("billInformation.csv", "a") as file:
        file.write(f"{roll},{collage},{semester},{department},{amount},{current_datetime},Semester Fee\n")

    # Add a confirmation message
    with open("accounts.csv", "r") as file2:
        for line in file2:
            account_info = line.strip().split(',')
            if account_info[1] == roll and account_info[4] == collage.upper() and account_info[2] == semester and \
                    account_info[3] == department.capitalize():
                old_Balance = int(account_info[5])
                account_info[5] = str(old_Balance - intAmount)
                print(f"{account_info[0]}, {amount}TK added your Semester Fee.")
            update_Contents.append(",".join(account_info))
    with open("accounts.csv", 'w') as file:
        for account_line in update_Contents:
            file.write(account_line + "\n")
    utilitis.menuPrint()


def canteenFee():
    update_Contents = []
    roll, collage, semester, department = payBill()
    amount = input("Enter Canteen Fee amount: ")
    intAmount = int(amount)
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("billInformation.csv", "a") as file:
        file.write(f"{roll},{collage},{semester},{department},{amount},{current_datetime},Canteen Fee\n")

    # Add a confirmation message
    with open("accounts.csv", "r") as file2:
        for line in file2:
            account_info = line.strip().split(',')
            if account_info[1] == roll and account_info[4] == collage.upper() and account_info[2] == semester and \
                    account_info[3] == department.capitalize():
                old_Balance = int(account_info[5])
                account_info[5] = str(old_Balance - intAmount)
                print(f"{account_info[0]}, {amount}TK added your Canteen Fee.")
            update_Contents.append(",".join(account_info))
    with open("accounts.csv", 'w') as file:
        for account_line in update_Contents:
            file.write(account_line + "\n")

    utilitis.menuPrint()


def billMenuPrint():
    for menu in menus:
        index = menus.index(menu)
        print(f"{index + 1}.", menu)
    choice = input("Enter your choice: ")
    if choice == "1":
        tuitionFee()
    elif choice == "2":
        semesterFee()
    elif choice == '3':
        canteenFee()
    elif choice == '4':
        utilitis.menuPrint()
    else:
        print("Invalid Choice")
