print('Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros números naturais.')
n = int(input('Digite um número: '))

soma = 0

if n > 0:
    for i in range (0, n +1):
        soma += i

else:
    print('Não é um número positivo')
    

print(soma)