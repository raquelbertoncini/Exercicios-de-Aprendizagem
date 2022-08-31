print('Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.')
import math
i = 1
lista = []
while i <= 10:
    num = int(input(f'Digite o número {i}: '))
    i += 1
    lista.append(num)

maior = max(lista)
menor = min(lista)
print(f' Da lista {lista}, o maior número é o {maior}, e o menor {menor}')