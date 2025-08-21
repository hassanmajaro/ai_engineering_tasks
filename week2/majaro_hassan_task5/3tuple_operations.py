''' Task3: Tuple Operations
    Create a tuple of 5 Nigerian states entered by the user.
    Print the first state and last state.
    Check if "Lagos" is in the tuple and print "Yes" or "No".
    Print the number of states entered.
'''
print("===Task 3===")
state1 = input("Enter a state: ").capitalize()
state2 = input("Enter 2nd state: ").capitalize()
state3 = input("Enter 3rd state: ").capitalize()
state4 = input("Enter 4th state: ").capitalize()
state5 = input("Enter 5th state: ").capitalize()
state = (state1, state2, state3, state4, state5)
print(f"first state is {state[0]}, and last state is {state[4]}")
print(f"Lagos in state?", "Lagos" in state)
print("no of state entered is", len(state))