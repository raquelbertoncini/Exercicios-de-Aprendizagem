print('Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E, conforme a fórmula a seguir:\n'
' E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!')

n = int(input('Digite um número inteiro positivo: '))
e = 1

for i in range(1, n+1):
    fatores = i

    for j in range(1, fatores):
        fatores *= j

        e += 1/fatores

print(f"O valor de E = {e}")