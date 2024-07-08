# Bomb - countdown

# Libray os - to acess the terminal windows
# Library Time to set the time 
import os
import time

count = int(input('Digite um número inteiro: '))

while count >= 0:

    os.system('cls')

    print(f'Contagem Regressiva {count}...')
    count -= 1

    time.sleep(1)

os.system('cls')
print('BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMMM')