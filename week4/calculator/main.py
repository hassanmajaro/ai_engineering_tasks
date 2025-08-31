from math_operations import *

def main():
    print("Basic Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponential (^)")
    print("6. Modulus (%)")
    print("7. Square Root (v)")
    print("8. Cube Root (3v)")
    print("9. Exit.")

    print("\nWhich operations would you like to perform?")

    while True:

        try:

            choice = int(input("Enter choice (1-8, 9 to exit): "))


            if choice in range(1, 7):
                num1 = float(input("Input first number: "))
                num2 = float(input("Input second number: "))

                if choice == 1:
                    print(f"{num1} + {num2} = {add(num1, num2)}\n")
                elif choice == 2:
                    print(f"{num1} - {num2} = {sub(num1, num2)}\n")
                elif choice == 3:
                    print(f"{num1} * {num2} = {mul(num1, num2)}\n")
                elif choice == 4:
                    print(f"{num1} / {num2} = {div(num1, num2)}\n")
                elif choice == 5:
                    print(f"{num1} ^ {num2} = {exp(num1, num2)}\n")
                elif choice == 6:
                    print(f"{num1} % {num2} = {mod(num1, num2)}\n")
            elif choice == 7:
                num3 = float(input("Input number: "))
                print(f"Square root of {num3} = {sq_root(num3)}\n")
            elif choice == 8:
                num4 = float(input("Input number: "))
                print(f"Cube root of {num4} = {cube_root(num4)}\n")
            elif choice == 9:
                print("Exiting... Thank you!")
                break
            else:
                print("Invalid option. Try Again.")

        except ValueError as ve:
            print("Error: ", ve, "\nTry again!")


main()