''' Task 2
    Comment the code below approximately, and using docstring, explain what the code is doing.
    Adapt the code to the case below
    Federal Government Scholarship Key Eligibility Requirements:
        Citizenship:
            Applicant must be a citizen of Nigeria
        Enrollment:
            Must be a registered, full-time undergraduate student in a recognized Nigerian university
        Other Scholarships:
            Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry whether national or international
        Academic Qualification:
            For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, 
            including English and Mathematics.
'''
''''
name = input("Enter your name: ")       # This prompts the user to input their name
age = int(input("Enter your age: "))    # This prompts the user for their age
score = int(input("Enter your test score: "))   # This prompts the user to input their test score

eligibility = (age < 18) and (score > 70)   # This checks that if the User is less than 18 and score is greater than 70; it will be true if both condition is met, if not false
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")
'''

print("===Federal Government Scholarship Eligibility===")
name = input("Enter your full name: ").title().split(" ")
citizenship = input("Are you a citizen of Nigeria? (Yes/No): ").capitalize()
age = int(input("Input your age: "))
enrollment = input("Are you a full-time student in a Nigeria University? (Yes/No): ").capitalize()
other_scholarship = input("Are you a beneficiary of another scholarship (Both National and International)? (Yes/No): ").capitalize()
qualification = int(input("Enter the number of grades in O'level (including English & Maths): "))

if citizenship == "Yes" and age >= 18 and enrollment == "Yes" and enrollment == "Yes" and other_scholarship == "No" and qualification >= 5:
    print(f"Congratulations {name[1]}! You are eligible for this scholarship")
else:
    print("You are not eligible for the Federal Government Scholarship")
