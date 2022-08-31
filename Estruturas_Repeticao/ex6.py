print('Faça um programa que leia 10 inteiros e imprima sua média')
count = 1
soma = 0
while count <=10:
    num = int(input(f'Digite o {count} número: '))
    count += 1
    soma += num
    media = soma / 10
print(media)