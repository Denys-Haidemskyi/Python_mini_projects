def Calculator():
    while True:
        first_number = float(input('Enter your number: '))
        operand = input('Enter operand (/, *, +, -): ')
        second_number = float(input('Enter your number: '))
        
        if operand == "+":
            print(f'Result: {first_number + second_number}')
        elif operand == "-":
            print(f'Result: {first_number - second_number}')
        elif operand == "*":
            print(f'Result: {first_number * second_number}')
        elif operand == "/":
            if second_number != 0:
                print(f'Result: {first_number / second_number}')
            else:
                print('Error, you are dividing by zero!')
        else:
            print('You entered an incorrect operand')

        qst = input('Do you want to perform the operation again? (yes/no)')
        if qst.lower() != 'yes':
            break;

Calculator()