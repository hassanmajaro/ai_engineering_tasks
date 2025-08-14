'''7. List Manipulation
'''
cities = ['Lagos', 'Abeokuta', 'Ibadan', 'Ijebu', 'Lekki']
print(cities)
city = input("enter 3rd city: ")
cities[2] = city
cities.remove("Lekki")
cities.insert(0, "Iwo")
print(cities)