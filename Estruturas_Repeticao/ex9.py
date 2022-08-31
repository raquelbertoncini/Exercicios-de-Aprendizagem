print('Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.')
num = int(input('Digite um número: '))
cont = 0


for i in range (1, num * num):
    if i % 2 == 1:
        cont += 1
        print(i)
    
        if cont >= num:
            break
print(f'total de números {cont}')