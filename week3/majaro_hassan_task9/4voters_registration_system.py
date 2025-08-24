''' Task4: Create a Unique Voters Registration System
    Ask for voter names and store in a set.
    If a voter tries to register twice, display a warning.
    After registration, display the total number of unique voters.
'''
voter_name = set()
name = input("Enter voter's name: ").capitalize()
voter_name.add(name)

name2 = input("Enter another voter's name: ").capitalize()
while True:
    if name2 in voter_name:
        print(f"{name2}. You have already voted")
        break
    else:
        voter_name.add(name2)
        print(f"Total number of voters are {len(voter_name)}")