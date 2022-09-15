print('Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saída o número de cada dado e a relação entre eles (>, <, =) de cada lançamento.')

from random import randint

n = int(input('Quantas vezes deseja jogar os dados? '))


d = 1

while d <= n:
    d1 = randint(1, 7)
    d2 = randint(1, 7)
    print('*'*10)

    print(f' {d}/{n}')
    if d1 > d2:
        print(f'Dado 1 ({d1}) > ({d2}) Dado 2 ')
    elif d1 == d2:
        print(f'Dado 1 ({d1}) empate ({d2}) Dado 2 ')
    elif d1 < d2:
        print(f'Dado 1 ({d1}) < ({d2}) Dado 2 ')

    d += 1

