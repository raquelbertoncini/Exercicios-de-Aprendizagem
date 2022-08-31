print('Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.')
count = 1
sum = 0
while count <= 10:
    num = int(input(f'Digite o {count} número: '))
    if num > 0:
        count += 1
        sum += num
    else:
        print('Este não é um número válido')
        continue
media = sum / 10
print(f'A média dos números é {media}')