from functionalities import addition, subtraction, multiplication, division
print("Hello World")

while True:
    ch = int(input("1. Addition\n2.Subtraction\n3.Multiplication\n4.Division\nEnter your choice: "))
    match ch:
        case 1:
            num1 = int(input("Enter First Number"))
            num2 = int(input("Enter Second Number"))
            print(addition(num1,num2))
        case 2:
            num1 = int(input("Enter First Number"))
            num2 = int(input("Enter Second Number"))
            print(subtraction(num1,num2))
        case 3:
            num1 = int(input("Enter First Number"))
            num2 = int(input("Enter Second Number"))
            print(multiplication(num1,num2))
        case 4:
            num1 = int(input("Enter First Number"))
            num2 = int(input("Enter Second Number"))
            print(division(num1,num2))
        case 0:
            break
        case _:
            print("Enter valid choice")
