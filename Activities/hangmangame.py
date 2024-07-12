import random
import time

wordLists = ['python', 'programação', 'computador', 'notebook', 'fullStack', 'Algortimo']

word = random.choice(wordLists)

correctLetters = []
incorrectLetters = []
attempts = 6

while True:
    hiddenWord = ''

    for letter in word:
        if letter in correctLetters and letter:
            hiddenWord += letter
        else:
            hiddenWord += '_'

    print('Palavra', hiddenWord)
    print('Letras erradas', incorrectLetters )
    print('Tentativas Restantes', attempts)

    if hiddenWord == word:
        print('Parabéns, você acertou a palavra!')
        break
    elif attempts== 0:
        print('Você perdeu, a palavra correta era :', word)

    letterUser = input('Digite uma letra :').lower()

    if letterUser in word:
        print('Você acertou a letra!')
        correctLetters.append(letterUser)
    else:
        print('Você errou a letra!')
        incorrectLetters.append(letterUser)
        attempts -= 1

