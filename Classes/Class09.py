name = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5', 'nome6', 'nome7']

# Remove the last item from the list or remove with the index of the list
name.pop() #index

# Remove a quantity determined of itens from the list or just one item
del name[2] # quantity

for i in range(len(name)):
    print(f'{i+1}° Nome da lista é: {name[i]}')


new_name = input('Digite o novo nome para inserir na lista: ')

position = input('Digite a posição que deseja adicionar na lista')
position = int(position)

position -= 1 # correct position

if position >= 0 and position <= len(name):
    name.insert(position, new_name)
else:
    print('Posição inválida')

# Current List
print()
print(30*'x', 'Lista Atualizada', 30*'x')

for i in range(len(name)):
    print(f'{i + 1}° Nome da lista é: {name[i]}')

#Replacement 
name[2] = 'garoto de programa'
print(name)

list1 = [1,2,3,5,5,7,8,9,2,4,6,8]
print(f'Lista desordenada {list1}')


# ascending ordered list
list1.sort(reverse=True)
print(f'Lista ordenada {list1}')

