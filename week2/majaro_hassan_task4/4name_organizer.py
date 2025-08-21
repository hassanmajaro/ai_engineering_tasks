''' 4. Name Organizer
    Ask the user to enter 5 names (separated by spaces)
    convert all names to lowercase
    sort the list alphabetically
    display them one name per line. Tips: use range(), sort(), for, in,
    split(), len(), lower()
'''
names = input("Enter 5 names separated by space: ")
conv = names.lower()
conv2 = conv.split()
conv2.sort()
print(conv2)
for name in conv2:
    print(name)