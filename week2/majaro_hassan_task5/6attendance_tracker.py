'''Task6: Attendance Tracker
    Write a Python program that;
    Stores the days of the week in a tuple.
    Stores the months of the year in another tuple.
    Asks the user to enter: student's name, gender, course track, current month number(1-12), current day number(1-7) and print
'''
print("===Task 6===")
days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
months_of_the_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
name = input("Enter Student Name: ")
age = input("Enter Gender: ")
course = input("Enter Course Track: ")
month = int(input("Enter Current Month in number(1-12): ")) - 1
day = int(input("Enter Current Day in number(1-7): ")) - 1

print("Days of the week", days_of_the_week)
print("Months of the year", months_of_the_year)
print(f'''
    Student Name:   {name}
    Student Age:    {age}
    Course Track:   {course}
    Current Month:  {months_of_the_year[month]}
    Current Day:    {days_of_the_week[day]}
''')