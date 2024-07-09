for i in range(0, 21):
    if i % 2 == 0 :
        print(i)


#Tree natalist 

height = 17
spacement = 0
asterisc = 1
simbol = '*'

for i in range(height):
    spacement = height - i - 1

    for j in range(spacement):
        print(' ', end='')

    for k in range(asterisc):
        print(simbol, end='')

    print()
    asterisc += 2

# List = []
lista = ['Nome1', 'Nome2', 'Nome3', 'Nome4', 'Nome5']

print(f'O primeiro nome da lista é {lista[0]}')
print(f'O Segundo nome da lista é {lista[1]}')

# range returns a sequence of numbers, starting from 0 by default

for i in range(len(lista)):
    print(f'Nome {i+1}: {lista[i]}')

#Tabuada

x = int(input('Digite um numero inteiro'))
for num in range(1, 11):
    print(f'{x} x {num} = {x*num}')

