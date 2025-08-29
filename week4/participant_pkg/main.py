from pathlib import Path
import file_ops


def work_path():
    workspace = Path("participant_pkg")
    workspace.mkdir(exist_ok=True)
    file_path = workspace / 'participants.csv'

def participant():

    while True:
        participant_data = {}

        while True:
            name = input("Enter name: ")
            if name.isalpha() and len(name) != 0:
                participant_data['name'] = name
                break
            print("Name must be alphabet and not empty")
            
        while True:
            age = input("Enter age: ")
            try:
                new_age = int(age) 
                participant_data['age'] = new_age
                break
            except ValueError:
                print('Age must be number')
                    
        while True:
            phone = input("Enter phone number: ")
            if phone.isdigit() and len(phone) == 11:
               participant_data['phone'] = phone
               break
            print("Phone number must be numbers and 11 digits")
                    
        while True:
            track = input("Enter track: ")
            if len(track) != 0:
                participant_data['track'] = track
                break
            print("Track cannot not be empty")

        return participant_data


def participant_list(n):
    path = work_path()
    for i in range(n):
        participant_dict = participant()
        file_ops.save_participant(path, participant_dict)

# n = int(input("How many participants do you want to add"))
# participant(n)

# all_participants = file_ops.load_participant(work_path())
# print(all_participants)

file_ops.load_participant(work_path())
participant()