voter_name = set()

try:
    name = input("Enter voter's name: ").strip().capitalize()

    if not name:
        raise ValueError("Name cannot be empty")
    
    voter_name.add(name)

    name2 = input("Enter another voter's name: ").strip().capitalize()

    if not name2:
        raise ValueError("Name cannot be empty.")
    
    while True:
        if name2 in voter_name:
            print(f"{name2}, you have already voted")
            break
        else:
            voter_name.add(name2)
            print(f"Total number of voters are {len(voter_name)}")
            break 

except ValueError as ve:
    print(f"Input Error: {ve}")
    
except Exception as e:
    print(f"Unexpected error occured: {e}")
