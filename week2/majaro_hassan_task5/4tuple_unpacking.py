''' Task4: Tuple Unpacking
    Ask a user for their;
    first name, age, favorite color, home town
    store them in a tuple profile and unpack into variables
    print and use escape sequence to align each piece of information nicely
'''
print("===Task 4===")
first_name = input("What is your first name? ")
age = int(input("What is your age? "))
fav_color = input("What is your favorite color? ")
home_town = input("What is your home town? ")

profile = (first_name, age, fav_color, home_town)
first_name, age, fav_color, home_town = profile
print(f"Name:\t\t{first_name}\nAge:\t\t{age}\nFav. Color:\t{fav_color}\nHome Town:\t{home_town}")