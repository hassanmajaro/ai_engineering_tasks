'''4. Name Organizer
'''
names = input("Enter 5 names separated by space: ")
conv = names.lower()
conv2 = conv.split()
conv2.sort()
for name in conv2:
    print(name)