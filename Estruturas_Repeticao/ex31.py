print('Faça um programa que calcule e escreva o valor de S:\n'
'S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/55')

n1 = 1
soma = 0

for n in range(1, 100, 2):
    s = n/n1
    n1 += 1
    soma += s

print(soma)
'''
Outra maneira:

s = 0
den = 1
for num in range(1, 100, 2):
    while den <= 50:
        s = s + (num / den)
        den = den + 1
        break
print(f'S = {s}')
'''