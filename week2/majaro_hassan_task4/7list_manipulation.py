''' 7. List Manipulation
    Create a list of five cities.
    Replace the third city with a new one (entere by the user).
    Remove the last city
    add a new city to the beginning of the list
    print the updated list
'''
cities = ['Lagos', 'Abeokuta', 'Ibadan', 'Ijebu', 'Lekki']
print(cities)
city = input("enter 3rd city: ")
cities[2] = city
cities.remove("Lekki")
cities.insert(0, "Iwo")
print(cities)