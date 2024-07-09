import os
import time

# Function to calculate the IMC value
def calculatorImc(name, weight, height):
    imc = weight / (height ** 2)
    print(f'Olá {name}, seu IMC é {imc:.2f}')
    if imc < 17:
        return 'Você está com anorexia.'
    elif imc < 18.5:
        return 'Você está abaixo do peso.'
    elif imc < 25:
        return 'Você está no peso ideal.'
    elif imc < 30:
        return 'Você está acima do peso.'
    elif imc < 35:
        return 'Você está com grau de obesidade I.'
    elif imc < 40:
        return 'Você está com grau de obesidade II.'
    else:
        return 'Você está com grau de obesidade mórbida.'

# Loop while to validate if the user want's to knwo your imc value
while True:
    validator = input('Deseja realizar um novo cálculo IMC ?\n Digite sim ou não:').lower()
    if validator == 'sim' or validator == 's':

        os.system('cls')
        name = input('Digite o seu nome: ')

        os.system('cls')
        print(f'Seja Bem-Vindo senhor(a){name} a calculadora IMC do Fabas')

        weight = float(input('Digite o seu peso(kg): '))
        height = float(input('Digite a sua altura(mt):'))

        os.system('cls')
        print(calculatorImc(name, weight, height))
    else:
        os.system('cls')
        print(f'Até mais {name}!')
        time.sleep(5)
        os.system('cls')
        break


        
    
