print('Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente.')
num = int(input('Digite um número: '))
if num > 0:
    for i in range(num, 0, -1):
        print(i)

else:
    print( 'Precisa ser um número positivo')