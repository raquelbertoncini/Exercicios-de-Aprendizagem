print('Faça um programa que receba dois números. Calcule e mostre:\n'
'- a soma dos números pares desse intervalo de números, incluindo os números digitados;\n'
'- a multiplicação dos números ímpares desse intervalo, incluindo os digitados.')
n1 = int(input('Digite o 1 número: '))
n2 = int(input('Digite o 2 número: '))
soma = 0
mult = 1
for i in range(n1, n2+1):
    if i % 2 == 0:
        soma += i
    elif i % 2 == 1:
        mult *= i
    else:
        print('Erro')

print(f'A soma dos pares: {soma}, a multiplicação dos ímpares é {mult}')