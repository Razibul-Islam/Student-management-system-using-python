import billPay
import utilitis


def addBalance():
    bill = billPay.inputValue()
    new_balance_len = input("Add New Balance: ")
    new_balance = int(new_balance_len)

    updated_accounts = []

    with open("accounts.csv", 'r') as file:
        for line in file:
            account_info = line.strip().split(",")
            if bill[0] == account_info[1] and bill[1].upper() == account_info[4] and bill[2] == account_info[2] and \
                    bill[3].capitalize() == account_info[3]:
                old_balance = int(account_info[5])
                account_info[5] = str(old_balance + new_balance)
            updated_accounts.append(','.join(account_info))
            # print(updated_accounts)

    # Write updated account info back to the file
    with open("accounts.csv", 'w') as file:
        for account_line in updated_accounts:
            file.write(account_line + '\n')
        print(f"Add Money Successfully to {account_info[0]}'s Account!")
    utilitis.menuPrint()
