from re import I


print('Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é 1+2+3+6+11+22+33 = 78')
n = int(input('Digite um número: '))
count = []
soma = 0
for i in range(1, n):
    if n % i == 0:
        soma += i
        count.append(i)
print(f'a soma dos números {count}, que são divisores de {n}, é igual a {soma}')
