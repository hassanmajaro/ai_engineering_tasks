import csv
from pathlib import Path

csv_file = Path.cwd()
filepath = csv_file / "details.csv"

while True:
    name = input("Enter name: ")
    if name.isalpha():
        str(name)
    else:
        print("Invalid input. Try again!")
        break
            
    age = input("Enter age: ")
    if age.isdigit():
        int(age)
    else:
        print()
        break

    phone = input("Enter phone number: ")
    if phone.isdigit():
        int(phone)
        break
    else:
        print("Invalid input. Try again")
        break

    # track = input("Input Track: ")
    # if track is not str:
    #     print("error")
    # else:
    #     print()

participant_details = [
    ["Name", "Age", "Phone Number", "Track"],
    [name, age, phone]
]


with open(filepath, "w", encoding="utf-8") as f:
    new = csv.writer(f)
    new.writerows(participant_details)