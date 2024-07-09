
# Atividade da Aula 2 0 Desenvolver um Sistema que receba o nome, idade, peso e altura de uma pessoa


name = input('Digite o seu nome: ')

age = int(input('Digite a sua idade: '))

weight = float(input('Digite o seu peso: '))
height = float(input('Digite a sua altura: '))

print(f'Seu nome é: {name}\n Sua idade é: {age}\n Seu peso é: {weight}\n Sua Altura é: {height}')
print(f'Tipos de dados: {type(name)}\n{type(age)}\n {type(weight)}\n {type(height)}')
