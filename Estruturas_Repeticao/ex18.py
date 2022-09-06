print('Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.')
n = int(input('Quantos números vc quer digitar? '))
import math
numeros = []
while len(numeros) < n:
    num = int(input('Digite o número: '))
    numeros.append(num)

maior = max(numeros)
print(maior)