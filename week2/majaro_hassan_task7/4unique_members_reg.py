''' Task4: Unique Members Registration
    Ask the user to enter three names separated by commas
        convert them to a set to ensure uniqueness
        create a dictionary where each name is a key and its length is the value.
    Requirements:
        use .split(",") and set() to remove duplicates.
        use dictionary comprehension {name: len(name) for name in set_of_names}
'''
names = input("Enter three names (separated by comma): ")
set_names = set(names.split(","))
dict_names = {name: len(name) for name in set_names}
print(dict_names)