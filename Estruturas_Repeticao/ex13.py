print('Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente.')
n = int(input('Digite o número: '))
count = 0

if n > 0:
    for i in range(0, n+1):
        if i % 2 == 0:
            count += 1
            print(i)