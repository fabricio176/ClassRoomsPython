import random

numberSecret = random.randint(1,30)

attempts = 0
maxAttempts = 5
win = False

print('Bem-vindo ao Python Games')
print(f'Você possui {maxAttempts} tentativas para adivinhar o número secreto entre 1 e 30')

while attempts < maxAttempts:
    hint = int(input('Digite um numero inteiro :'))
    attempts += 1

    if hint == numberSecret:
        win = True
    elif hint < numberSecret:
        print('Você errou! O número secreto é maior')
        print(f'Você ainda tem {maxAttempts - attempts} tentativas')
    elif hint > numberSecret:
        print('Você errou! O número secreto é menor')
        print(f'Você ainda tem {maxAttempts - attempts} tentativas')
    
if win:
    print(f'Parabéns, você acertou!\n O Número é: {numberSecret}\n Você precisou de {attempts} tentativas para acertar')
else:
    print(f'Que pena! Você não conseguiu adivinhar o número secreto, o número secreto era {numberSecret}')