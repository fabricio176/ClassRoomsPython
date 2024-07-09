import random 
import os

list = []
listprizers = []
while True:
    name = input('Digite os nomes que serão sorteados: ')
    if name != '':
        list.append(name)
    else:
        break

while True:
    if list:
        os.system('cls')
        prizer = random.choice(list)
        listprizers.append(prizer)
        

        print(f'O vencedor é {prizer}')
        list.remove(prizer)

        option = input('Deseja realizar um novo sorteio? (s/n)'.lower())
        os.system('cls')

        if option != 's':
            break
    else:
        print('Não há mais nomes para sortear.')
        break

completeList = list + listprizers
print(f'Lista completa {completeList}')
print(f'Lista dos não sorteados {list}')
print(f'Lista dos sorteados {listprizers}')
print('Sistema finalizado')