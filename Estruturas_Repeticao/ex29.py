print('Escreva um programa para calcular o valor da série, para 5 termos.\n'
'S = 0 + 1/2! + 2/4! + 3/6! + ...')
import math

n = 5
n1 = 1
n2 = 1
soma = 0

for i in range(1,6):

    valor = n1/(math.factorial(n2*2))
    n1 += 1
    n2 += 1
    soma += valor

print(valor)

'''
Outra maneira: 

print("Iniciando a execução.")
res = 0
den = 2
for num in range(1, 6):
    while den <= 10:
        res = num / (math.factorial(den))
        den = den + 2
        break
print(f'O resultado desejado é {res}')
'''
