print('Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem crescente.')
n = int(input('Digite um número ímpar: '))
if n > 0 and n % 2 == 1:
    for i in range(0, n+1):
        if i % 2 == 1:
            print(i)
else:
    print('Acho que foi pedido um número ímpar.')