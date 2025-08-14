''' Task3: Tuple Operations
    Create a tuple of 5 Nigerian states entered by the user.
    Printe the first state and last state.
    Check if "Lagos" is in the tuple and print "Yes" or "No".
    Print the number of states entered.
'''
print("===Task 3===")
state1 = input("Enter a state: ")
state2 = input("Enter 2nd state: ")
state3 = input("Enter 3rd state: ")
state4 = input("Enter 4th state: ")
state5 = input("Enter 5th state: ")
state = (state1, state2, state3, state4, state5)
print(f"first state is {state[0]}, and last state is {state[4]}")
print("Lagos" in state)
print("no of state entered is", len(state))