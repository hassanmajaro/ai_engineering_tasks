''' Task1: Student Bio Data Storage
    Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary
        Courses should be stored as a list
        Display the bio-data neatly using escape sequences.
    Requirements:
        use input() to collect details
        use dictionary operations (dict[key] = value) to store data.
        use print() formatting with \n and \t for better output.
'''
name = input("Name: ")
age = int(input("Age: "))
gender = input("Gender: ")
courses = input("Courses: ")

student = {
    "name": name,
    "age": age,
    "gender": gender,
    "courses": [courses]
}
print("\nStudent Bio-Data")
print(f"Name: \t\t{student["name"]}\nAge: \t\t{student["age"]}\nGender: \t{student["gender"]}\nCourses: \t{student["courses"]}")
