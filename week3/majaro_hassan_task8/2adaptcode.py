''' Task 2
    Comment the code below approximately, and using docstring, explain what the code is doing.
    Adapt the code to the case below
    Federal Government Scholarship Key Eligibility Requirements:
        Citizenship:
            Applicant must be a citizen of Nigeria
        Enrollment:
            Must be a registered, full-time undergraduate student in a recognized Nigerian university
        Other Scholarships:
            Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industrym whether national or international
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

name = input("Enter your name: ")
citizenship = input("Are you a Nigerian citizen? (Yes/No): ").lower()
enrollment = input("Are you a full-time undergraduate in a Nigerian University? (Yes/No): ")
scholarship = input("Are you currently on any Oil and Gas Scholarship? (Yes/No): ")
waec_result = int(input("Enter the number of WAEC distinctions you have (including English & Maths) i.e A/B grades: "))

requirements = [
    (citizenship == "yes"),
    (enrollment == "yes"),
    (scholarship == "no"),
    (waec_result >= 5)
]

eligibility = True
for rule in requirements:
    eligibility = eligibility and rule

print("Scholarship Application Result")
print(f"Candidate name: {name}")
print(f"Nigeria? ")
print(f"FT Undergraduate? {enrollment}")
print(f"Been on Oil & Gas Scholarship: {scholarship}")
print(f"Number of distinctions: {waec_result}")
print(f"Eligible: {eligibility}")