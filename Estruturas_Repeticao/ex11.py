print('Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente.')
num = int(input('Digite um número: '))
if num > 0:
    for i in range(0, num):
        print(i)

else:
    print( 'Precisa ser um número positivo')