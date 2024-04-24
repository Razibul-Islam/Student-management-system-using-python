import billPay
import addBalance
import allStudent
import updateDeleteStudent
import authentication
import qrCode

# Menu List
Menus = ["Pay Fees or Expenses", "Add Digital Balance or Money", "View All Student", "qrcode generator", "Delete "
                                                                                                         "Student",
         "Sign out"]


def menuPrint():
    for menu in Menus:
        index = Menus.index(menu)
        print(f"{index + 1}.", menu)
    choice = input("Enter Your Choice: ")
    if choice == "1":
        billPay.billMenuPrint()
    elif choice == "2":
        addBalance.addBalance()
    elif choice == "3":
        allStudent.viewAllStudent()
    elif choice == "4":
        qrCode.qrGenerator()
    elif choice == "5":
        updateDeleteStudent.deleteStudent()
    elif choice == "6":
        print("Sign Out Successfully!")
        authentication.main()
    else:
        print("Invalid Choice")
