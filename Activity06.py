# TODO: Resposta desafio 01
print('Seja Bem Vindo à brinquedoteca KidsBoy')

name = input('Digite o nome da Criança : ')
age = int(input('Digite a idade da Criança :'))
height = float(input('Digite a altura da Criança : '))

def canPlay(name, age, height):
    print(f'Olá {name} você Pode brincar no brinquedo' if age > 12 and height > 1.20 else 'Sinto muito {name}, você não pode brincar no brinquedo :()')

canPlay(name, age, height)

# TODO: Resposta desafio 02
name = input('Digite o nome do Aluno: ')

humor = input('Você acordou de bom humor ?\nDigite sim ou não').lower()
if humor == 'sim':
    humorBoolean = True
else:
    humorBoolean = False

parent_home = input('O Pai ja chegou em casa para leva-lo?\nDigite sim ou não ').lower()
if parent_home == 'sim':
    parentBoolean = True
else:
    parentBoolean = False

def checkGoToBeach(name, humorBoolean, parentBoolean):
    if(humorBoolean and parentBoolean): return print(f'{name} você pode ir à praia')
    else: return print(f'{name} você não pode ir à praia')

checkGoToBeach(name, humorBoolean, parentBoolean)

# TODO: Resposta desafio 03

def formatCpf(cpf):
    cpf_formated = cpf.replace(".", "").replace("-", "")
    cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]

    return cpf_formated

cpf = input('Digite o seu cpf com pontuação: ')
if(len(cpf) > 14):
    print('CPF deve ter menos que 11 números, digite novamente')
    cpf = input('Digite o seu CPF')
elif(len(cpf) < 14):
    print('CPF deve ter mais que 10 números, digite novamente')
    cpf = input('Digite o seu CPF')
else:
    print('CPF:', cpf)
    print('CPF sem modificações:', cpf)
    # Modificando o CPF
    cpfFormated = formatCpf(cpf)
    print('CPF modificado:', cpfFormated)

    # TODO: Resposta desafio 04

print('Seja Bem-Vindo a calculadora IMC do Fabas')

name = input('Digite o seu nome: ')

weight = float(input('Digite o seu peso(kg): '))
height = float(input('Digite a sua altura(mt)'))

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
    
print(calculatorImc(name, weight, height))

# TODO: Resposta desafio 05

print('Seja Bem-Vindo a Calculadora Simples do Fabas')
print('Para começar, digite dois números')

num1 = float(input('Digite o primeiro número'))
num2 = float(input('Digite o segundo número'))

sum = num1 + num2
subtraction = num1 - num2
division = num1 / num2
multiplication = num1 * num2

print('Soma:', sum)

print('Subtração:', subtraction)

print(f'Divisão: {division:,.2f}')

print('Multiplicação:', multiplication)
