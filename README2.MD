## Class 05 - Conditional

<h4>Structure Decision</h4>

* if
* else
* elif(Used when the decision is not used for the first time and need a condition)

## Class 06 - Operator Ternary

* Use operator ternary when the alternative are smallest and when have two or three alternatives

<h4>Replace</h4>

    peso = input('Digite o seu peso').replace('1', '0')
    print(type(peso))
    peso = float(peso)
    print(type(peso))

## Class 07 - While loop

While is a loop that repeat a algorithm while one determined condition is true.

<h4>While count until the number 10 is reached<h4>

    numero = 0

    while numero <= 10:
    print(numero)
    numero += 1 

    count = 0

    while count < 10
        count += 1
        if count % 2 == 0:
            print(count)
        elif count >= 7:
            break
        else:
            continue

        print('Contando...')

<kbd>pass - skip the pad code<kbd><br>
<kbd>continue - continue the code<kbd><br>
<KBD>While True - is a infinit loop</KBD>

    while True:
        nome = input('Informe o seu nome ou deixe em branco para sair)

        if nome != '':
            idade = int(input(Informe sua idade))

            if idade >= 18
    
## Class 08 - For loop

    for n in range(5)
        print(n)

    nome = ['joao', 'lucas', 'fabas', 'jonatas', 'cone']
    for n in nome:
        print(n)