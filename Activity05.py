# Number 

# Validation 

# number = int(input('Digite um número :'))

# # Function to check if a number is even

# def checkNumberEven(number):
#     if number % 2 == 0:
#         return print('Número digitado par :' + str(number))
#     else:
#         return print('Número digitado impar')
    
# checkNumberEven(number)

# # Challenge 02
# weightUser = float(input('Digite o seu peso'))
# weightElevator = float(input('Digite o peso da carga a ser tranposrtada: '))

# def checkWeightElevator(weightUser,weightElevator):
#     if (weightElevator + weightUser <= 200):
#         return print('Peso dentro dos limites')
#     else:
#         return print('Peso ultrapassou os limites')
    
# checkWeightElevator(weightUser,weightElevator)

# Challenge 03

name = input('Digite o seu nome : ')
age = int(input('Digite a a sua idade : '))
cpf = input('Digite o seu CPF : ')

grade1 = int(input('Digite a do Primeiro Bimestre: '))
grade2 = int(input('Digite a do Segundo Bimestre: '))
grade3 = int(input('Digite a do Terceiro Bimestre: '))
grade4 = int(input('Digite a do Quarto Bimestre: '))

totalGrade = grade1 + grade2 + grade3 + grade4

def averageStudent(totalGrade):
    avgGrade = totalGrade/4 

    if avgGrade >= 7:
        result = 'Aprovado'
        return result
    elif avgGrade >= 5:
        result = 'Recuperação'
        return result
    else:
        result = 'Reprovado'
        return result

def takeGrade(name, age, cpf, grade1, grade2, grade3, grade4):
    if(age >= 18):
        print(f'\nBoletim \n Nome: {name}\nCPF: {cpf}\n Nota 1° Bimestre: {grade1}\n Nota 2° Bimestre: {grade2}\n Nota 3° Bimestre: {grade3}\n Nota 4° Bimestre: {grade4}\n Média : {totalGrade/4} \n Resultado: {averageStudent(totalGrade)}')
    else:
        print(f'Estudante {name} menor de idade, por favor compareça com o seu responsável para retirar o seu boletim.')

takeGrade(name, age, cpf, grade1, grade2, grade3, grade4)

