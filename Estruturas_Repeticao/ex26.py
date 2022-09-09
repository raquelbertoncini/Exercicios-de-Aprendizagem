print('Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.')

num = int(input('Entre com um número: '))
while True:
    if num % 11 == 0:
        print(f'{num} é múltiplo de 11.')
        break
    elif num % 13 == 0:
        print(f'{num} é múltiplo de 13.')
        break
    elif num % 17 == 0:
        print(f'{num} é múltiplo de 17.')
        break
    num += 1

''' Se quiséssemos achar um múltiplo de cada um dos números, retirar os 'breaks', somente deixar o úlitmo'''