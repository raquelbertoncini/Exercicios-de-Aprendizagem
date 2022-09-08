print("Faça um algoritmo que leia um número positivo e imprima seus divisores.")
n = int(input('Digite um valor: '))
for i in range (1, n+1):
    if n % i == 0:
        print(f'O número {i} é divisor de {n}')
