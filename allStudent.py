import utilitis


def viewAllStudent():
    print("Only Admin Can Access This!")
    pin = "1111"
    password = "1212"

    Pin = input("Enter Your Pin(Admin Pin: 1111): ")
    Password = input("Enter Your Password(Admin Pass: 1212): ")
    if Pin == pin and Password == password:
        with open("accounts.csv", 'r') as file:
            headers = file.readline().strip().split(',')
            for line in file:
                values = line.strip().split(',')
                account_dict = dict(zip(headers, values[:-1]))
                print(account_dict)

        while True:
            inputChoice = input("To go back to the main menu, Enter 1: ")
            if inputChoice == "1":
                utilitis.menuPrint()
                break
            else:
                print("Please Enter 1")

