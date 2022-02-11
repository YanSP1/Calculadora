operation = input('''
_______________Welcome to the BeyondCalculator_________________
|Please type in the math operation you would like to complete:|
|+ for addition                                               |
|- for subtraction                                            |
|* for multiplication                                         |
|/ for division                                               |
|i for imc                                                    |
|_____________________________________________________________|
''')

if operation == '+':
        num1 = float(input('|Please enter the first number = '))
        num2 = float(input('|Please enter the second number = '))
        print('|{} + {} ='.format(num1, num2), num1 + num2, '|')

elif operation == '-':
        num1 = float(input('|Please enter the first number = '))
        num2 = float(input('|Please enter the second number = '))
        print('|{} - {} ='.format(num1, num2), num1 - num2, '|')

elif operation == '*':
        num1 = float(input('|Please enter the first number = '))
        num2 = float(input('|Please enter the second number = '))
        print('|{} * {} ='.format(num1, num2), num1 * num2, '|')

elif operation == '/':
        num1 = float(input('|Please enter the first number = '))
        num2 = float(input('|Please enter the second number = '))
        print('|{} / {} ='.format(num1, num2), num1 / num2, '|')
    
elif operation == 'i':
        num1 = float(input('|Please enter your Weight(KG) = '))
        num2 = float(input('|Please enter your height(M) = '))
        imc = num1/ (num2 * num2)
        print('|{} / ({} * {}) ='.format(num1, num2, num2), imc)

        if (imc == 0) or (imc <= 18.5):
            print('|Você está abaixo do peso|')

        elif (imc == 18.5) or (imc <= 24.9):
            print('|Você está em um peso adequadamente saúdavel|')
        
        elif (imc == 25) or (imc <= 29.9):
            print('|Você está em um estado de sobrepeso|')

        elif (imc == 30) or ( imc <= 39.9):
            print('|Você está em um estado de obesidade|')

        elif (imc >= 40):
            print('|Você está em um estado de obesidade mórbida|')

        else:
            print('|You have not typed a valid operator, please run the program again.')

else:
        print('You have not typed a valid operator, please run the program again.')
