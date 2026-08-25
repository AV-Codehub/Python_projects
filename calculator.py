print("MY FIRST CALCULATOR")

A = float (input("enter the first number: "))
operation = input("Enter the operation (+,-,*,/,%,**) : ")
B = float (input("enter the second number: "))

if operation == '+':
    print(A + B)
elif operation == '-':
    print(A - B)
elif operation == '*':
    print(A * B)
elif operation == '/':
    if B == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(A / B)
elif operation == '%':
    if B == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(A % B)
elif operation == '**':
    print(A ** B)
print("Thank you for using the calculator!")
