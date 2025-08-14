'''Task 4
    1. Your Favorite Life Quote
    Ask the user to input their favorite quiote.
    Convert it to title case
    Print it with quotation marks using escape sequences.
'''
quote = input("Input your favorite quote: ")
conv = quote.title()
print(f"Fav. Quote - \"{conv}\"")