import os
import time

clear = os.system('cls')

while True:
    validator = input('Você deseja entrar na calculadora do Fabas?\n Digite sim ou não: ').lower()

    if validator == 'sim' or 's':
        time.sleep(1)
        clear
        print(50*'-')
        print('Seja Bem-Vindo a Calculadora Simples do Fabas')
        print('Para começar, digite dois números')

        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        clear


        option = input('Qual operação deseja realizar ?\n 1 - Somar\n 2 - Subtrair\n 3- Dividir\n 4 - Multiplicar: ')
        clear
        
        if option == '1':

            print('Você escolheu a opção de somar.')
            sum = num1 + num2
            print('A Soma é igual a:', sum)

        elif option == '2':

            print('Você escolheu a opção de subtrair.')
            subtraction = num1 - num2
            print('A Subtração é igual a:', subtraction)

        elif option == '3':

            print('Você escolheu a opção de dividir.')

            if num2 == 0:
                print('Não é possível dividir por zero.')
            else:
                division = num1 / num2
                print('A Divisão é igual a:', division)

        elif option == '4':
            print('Você escolheu a opção de multiplicar.')
            multiplication = num1 * num2
            print('A Multiplicação é igual a:', multiplication)

        else:
            clear
            print('Opção inválida!')
            break
    else:
        clear
        print('Opção inválida!')
        break
    




