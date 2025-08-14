''' Task4: Create a Unique Voters Registration System
    Ask for voter names and store in a set.
    If a voter tries to register twice, display a warning.
    After registration, display the total number of unique voters.
'''
voters = set()
voter1 = input("Input voter name: ")
voter2 = input("Input 2nd voters name: ")
voter3 = input("Input 3rd voters name: ")
voters.add(voter1)
voters.add(voter2)
voters.add(voter3)

for voter in voters:
    print("Warning!")

print("Total number of voters are", len(voters))