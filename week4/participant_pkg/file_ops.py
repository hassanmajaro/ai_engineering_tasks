# helper module

import csv 
from pathlib import Path 

def save_participant(path, participant_dict):
    if path.exists():
        with open(path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(participant_dict.values())
    else:
        with open(path, "w", newline="", encoding="utf-8") as f:
            f.write("Name, Age, Phone, Track\n")
            writer = csv.writer(f)
            writer.writerow(participant_dict.values())
    
def load_participant(path):
    participants = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for c, row in enumerate(reader):
            if c == 0:
                continue 
            name, age, phone, track = row 
            participants.append({
                'name': name,
                'age': age,
                'phone': phone,
                'track': track
            })
            
    return participants