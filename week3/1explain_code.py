''' Task 1
        Explain each outpuut of the program below
        Give 3 use cases or scenarios where you can apply the program below
        Write the code for 1 of the 3 use cases.
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} : {num1 == num2}")
# This says num1 is equal to num2; then return true if it is and false if it's not
print(f"{num1} != {num2} : {num1 != num2}")
# This says num1 is not equal to num2; then return true if it is and false if it's not
print(f"{num1} > {num2} : {num1 > num2}")
# This says num1 is greater than num2; then return true if it is and false if it's not
print(f"{num1} < {num2} : {num1 < num2}")
# This says num1 is less than num2; then return true if it is and false if it's not
''' Use cases: 
    This program can be used the following cases:
    1.  It can be used for profit or loss
    2.  It can be used for age range classification
    3.  It can be used for eligibility check
'''
age = int(input("Input age: "))

infant = age < 1
toddlers = age >= 1 and age <= 3
child = age >= 4 and age <= 12
teenager = (age >= 13) and (age <= 19)
adult = age >= 20
print("Age classification")
print(f"Age: {age}\nInfant: {infant}\nToddlers: {toddlers}\nChild: {child}\nTeenager: {teenager}\nAdult: {adult}")