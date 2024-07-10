# # TODO: Resposta do desafio 01
# oddNumbers = []
# qtt = 100

# for i in range(1, qtt):
#     if i % 2 != 0:
#         oddNumbers.append(i)

# print(f'Foram encontrados {len(oddNumbers)} números impares')
# print(f'A Soma desses números é: {sum(oddNumbers)}')

# # TODO: Resposta do desafio 02
# taskList = []

# while True:
#     task = input('Você deseja adicionar uma nova Tarefa ?\n Digite Sim ou Não : ').lower()

#     if task == 'sim' or task == 's':

#         newTask = input('Digite o nome da nova tarefa: ')

#         taskList.append(newTask)

#         print(f'Tarefa {newTask} adicionada com sucesso!')
#     else:
#         print('Programa encerrado!')
#         break

# print(30*'x', 'Lista de Tarefas', 30*'x')

# for i,task in enumerate(taskList, start=1):
#     print(f'Tarefa {i}: {task} ')

# TODO: Resposta do desafio 03

number = int(input('Digite um número: '))

isPrime = 0
numberDivisible = []


for i in range(1, (number + 1)):        
    if number % i == 0:
        numberDivisible.append(i)
        isPrime += 1
    
if isPrime  == 2 :
    print(f'Número {number} é primo')
else:
    print(f'Número {number} Não é primo')
    

print('A quantidade de números divisíveis é:', len(numberDivisible))