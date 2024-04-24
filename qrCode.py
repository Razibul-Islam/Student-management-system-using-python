import qrcode
import json
import utilitis


def qrGenerator():
    roll = input("Enter your roll: ")
    with open("accounts.csv", "r") as file:
        for line in file:
            account_info = line.strip().split(",")
            if account_info[1] == roll:
                studentInfo = {"name": account_info[0], "Roll": account_info[1], "Semester": account_info[2],
                               "Department": account_info[3], "College Name": account_info[4],
                               "Current Balance": account_info[5]}
                # Convert studentInfo dictionary to a JSON string
                studentInfo_json = json.dumps(studentInfo)

                qr = qrcode.make(studentInfo_json)
                qr.save(f"{account_info[0]}'s_information.jpg")
                print("QR code created successfully!...")