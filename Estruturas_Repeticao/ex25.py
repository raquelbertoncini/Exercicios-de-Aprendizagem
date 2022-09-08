print('Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.')
soma = 0
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(f'A soma dos números múltiplos de 3 ou 5 é igual a {soma}')