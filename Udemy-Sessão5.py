'''print('1_ Faça um programa que receba dois números e mostre qual deles é o maior.')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
num = [n1, n2]
print(max(num))
print('-'*30)

import math
print('2_ Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada, se for negativo, mostre uma mensagem dizendo que o número é inválido.')
n = float(input('Digite um número: '))
if n < 0:
    print('Você não digitou um número válido!')
elif n > 0:
    n2 = math.sqrt(n)
    print(f'A raiz quadrada de {n} é {n2:.2f}')
print('-'*30)

print('3_ Leia um número real. Se o número for positivo imprima raiz quadrada. Do contrário, imprima o número ao quadrado.')
n1 = float(input('Digite um número: '))
import math
if n1 > 0:
    n2 = math.sqrt(n1)
    print(f'A raiz quadrada de {n1} é {n2:.2f}.')
elif n1 < 0:
    n2 = n1**2
    print(f'O quadrado de {n1} é {n2}.')
print('-'*30)

print('4_ Faça um programa que leia um número e, caso ele seja positivo, calcule o mostre: 1) o número digitado ao quadrado; 2) a raiz quadrada do número digitado.')
n = float(input('Digite um número: '))
from math import pow
if n < 0:
    print('Só estou aceitando números positivos. Operação encerrada.')
else:
    quadrado = n * n
    raiz = pow(n, 1/2)
    print(f'O quadrado de {n} é {quadrado}, e sua raiz quadrada é {raiz:.2f}.')
print('-'*30)

print('5_ Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.')
n = int(input('Qual é o seu número? '))
if n %2 == 0:
    print('Seu número é par!')
else:
    print('O número digitado é ímpar.')
print('-'*30)

print('6_ Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
maior = max(n1,n2)
diferenca = max(n1, n2) - min(n1,n2)
print(f'Dados os números {n1} e {n2}, o maior deles é o {maior}, a diferença entre os dois é {diferenca}.')
print('-'*30)

print('7_ Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem: números iguais.')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
maior = max(n1, n2)
if n1==n2:
    print('Eles são iguais!')
else:
    print(f'O maior número é: {maior}.')
'''
# 8, 9, 10, 11, 12