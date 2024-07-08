# Activity Cinema

import secrets
import os
import time


movieList = ['Meu Malvado Favorito 4 SALA 1 - Livre ', 'MaXXXine SALA 2 - Maiores de 18 Anos', 'Divertida Mente 2 SALA 3 - Livre', 'Entrevista Com O Demônio SALA 4 - Maiores de 18 anos', 'Deadpool & Wolverine SALA 5 - Maiores de 18 anos']
optionInvalid = False

while True:
    if optionInvalid == False:
        print(50*'-')
        print('Seja bem-vindo ao cinema do Fabas')
        print(50*'-')

        name = input('Informe o seu nome: ').upper()
        age = int(input('informe sua idade: '))
        os.system('cls')

    print(f'Filmes em cartaz')
    for i, movie in enumerate(movieList, start=1):
        print(f'{i} - {movie.strip()}')
    option = int(input('Escolha um Filme: '))

    if option == 2 or option == 4 or option == 5:
        if age >= 18:
            ingresso = secrets.token_hex(8)
            print(f'Você está apto para assistir {movieList[option-1].strip()}')
            print(f'{name}, o seu ingresso é {ingresso}')     
        else:
            optionInvalid = True
            print('Você não está apto para assistir este filme.\n Tente Novamente')
            time.sleep(2)
            os.system('cls')
    elif option == 1 or 3:
        ingresso = secrets.token_hex(8)
        print(f'Você está apto para assistir {movieList[option-1].strip()}')
        print(f'{name}, o seu ingresso é {ingresso}')
        break
    else:
        optionInvalid = True
        print('Opção inválida.\n Tente Novamente')
        time.sleep(2)
        os.system('cls')
        continue

