def calculator():
    print("Welcome to the Simple Calculator!")
    
    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        operation = input("Enter the number corresponding to your choice (1-5): ")
        
        if operation == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        if operation not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue
        
        if operation == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")

# Call the calculator function
calculator()
