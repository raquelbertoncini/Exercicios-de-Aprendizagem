print('Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente.')
n = int(input("Digite um número de 3 dígitos pra ficar legal: "))
count = 0

if n > 0:
    for i in range(n, 0, -1):
        if i % 2 == 0:
            print(i)
            count += 1
    print(f' Quantidade total de números {count}')