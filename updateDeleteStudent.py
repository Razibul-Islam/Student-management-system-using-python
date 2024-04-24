import billPay
import utilitis

def deleteStudent():
    info = billPay.inputValue()
    updated_accounts = []

    with open("accounts.csv", 'r') as file:
        for line in file:
            studentInfo = line.strip().split(",")
            if studentInfo[1] != info[0] or studentInfo[4] != info[1].upper() or studentInfo[2] != info[2] or \
                    studentInfo[3] != info[3].capitalize():
                updated_accounts.append(','.join(studentInfo))

    with open("accounts.csv", 'w') as file:
        for account_line in updated_accounts:
            file.write(account_line + '\n')
        print("Student deleted successfully")
    utilitis.menuPrint()


