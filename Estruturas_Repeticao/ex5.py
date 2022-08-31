print('Faça um programa que peça ao usuário para digitar 10 valores e some-os.')
cont = 1
soma = 0
while cont <=10:
    num = int(input(f'Digite número {cont}: '))
    cont += 1
    soma += num
print(num)