print('Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem decrescente.')
n = int(input('Digite um número ímpar, de no mínimo 2 dígitos: '))
if n > 0 and n % 2 == 1:
    for i in range(n, 0, -1):
        if i % 2== 1:
            print(i)