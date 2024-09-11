while True:
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))

    print("The operations are as follows:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    operation = int(input("Choose Operation : "))

    if operation == 1:
        c = a + b
        print("Answer :", c)
    elif operation == 2:
        c = a - b
        print("Answer :", c)
    elif operation == 3:
        c = a * b
        print("Answer :", c)
    elif operation == 4:
        c = a / b
        print("Answer :", c)
    elif operation == 5:
        break
    else:
        print("Wrong Operation")
