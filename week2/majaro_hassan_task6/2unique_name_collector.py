''' Task2: Unique Name Collector
    Write a program that collects the names of people 
    attending a seminar (no duplicates allowed) and displays 
    them in alphabetical order
'''
people = input("Enter the name of people attending a seminar (separated by comma): ")

# name_of_people = people.split()
attendance = set(people.split(','))
sorting = sorted(attendance)
print(sorting)