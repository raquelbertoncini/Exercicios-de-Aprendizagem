print('Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos que compõe o número.')
# modo 1
'''n = int(input('Digite um número entre 100 e 999: '))
if 100 <= n <= 999:
    num = str(n)
    print(num[0])
    print(num[1])
    print(num[2])
else:
    print('Número fora da faixa')
'''
#modo 2
n = int(input('Digite um número entre 100 e 999: '))
if 100 <= n <= 999:
    lista = str(n)

    print("Cada algarismo que compõem o número:")
    for x, y in enumerate(lista):
        print(y)