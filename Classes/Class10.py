import os
import time

listCpf = ['12345678910', '12345678911', '12345678912', '12345678913']
listUsers = ['user1', 'user2', 'user3', 'user4']

while True:
    print(15*'x' + ' Seja Bem-vindo ao Menu' + 15*'x')
    print(f'1 - Cadastrar Usuario')
    print(f'2 - Consultar Usuários')
    print(f'3 - Remover Usuário')
    print(f'4 - Sair')

    option = int(input('Selecione uma Opção:'))

    os.system('cls')

    if option == 1:
        cpf = input('Digite o CPF do Usuário: ')
        username = input('Digite o Nome de Usuário: ')

        if cpf in listCpf:
            print('CPF já cadastrado, tente novamente.')
        else:
            listCpf.append(cpf)
            listUsers.append(username)
            print('Usuário cadastrado com sucesso.')
    
    elif option == 2:
        i=1
        for users, cpf in zip(listUsers, listCpf):
            print(f'Usuário {i} - {users} - {cpf}')
            i += 1
    
    elif option == 3:
        cpf = input('Digite o CPF do Usuário: ')

        if cpf in listCpf:
            index = listCpf.index(cpf)
            listCpf.pop(index)
            listUsers.pop(index)
            print('Usuário removido com sucesso.')
    else:
        print('Encerrando programa.')
        time.sleep(5)
        break
        