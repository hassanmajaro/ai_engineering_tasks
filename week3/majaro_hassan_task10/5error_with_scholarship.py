print("=== Federal Government Scholarship Eligibility ===")

try:
    name = input("Enter your full name: ").title().split(" ")

    if len(name) < 2:
        raise ValueError("Enter your full name (first and last).")
    
    citizenship = input("Are you a citizen of Nigeria? (Yes/No): ").capitalize()
    age = int(input("Enter your age: "))
    enrollment = input("Are you a full-time student in a Nigerian University? (Yes/No): ").capitalize()
    other_scholarship = input("Are you a beneficiary of another scholarship (both National and International)? (Yes/No): ").capitalize()
    qualification = int(input("Enter the number of grades in O'level (including English & Maths): "))

    if citizenship == "Yes" and age >= 18 and enrollment == "Yes" and other_scholarship == "No" and qualification >= 5:
        print(f"Congratulations {name[1]}! You are eligible for this scholarship")
    else:
        print("You are not eligible for the Federal Government Scholarship")

except ValueError as ve:
    print("Input Error: {ve}")
except Exception as e:
    print("Unexpected error occured: {e}")
