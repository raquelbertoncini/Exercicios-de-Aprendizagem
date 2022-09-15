print('Faça programas para calcular as seguintes sequências:\n'
'1_ 1+ 2 + 3 + 4 + 5 + ... + n\n'
'2_ 1 - 2 + 3 - 4 + 5 + ... + (2n-1)\n'
'3_ 1 + 3 + 5 + 7 + ... + (2n - 1)')

n = int(input('Digite o número final:  '))

#sequencia 1

soma1 = 0

for num in range(1, n+1):
    soma1 += num

print(f'A soma do exercício 1 é: {soma1}')


#sequencia 2

somaimpar = 0
somapar = 0

for num in range (1, n+1):
    if num % 2 == 0:
        somapar += num
    elif num % 2 == 1:
        somaimpar += num

soma2 = somaimpar - somapar
print(f'A soma do exercício 2 é: {soma2}')

#sequencia 3

soma3 = 0

for num in range(1, n+1, 2):
    soma3 += num
print(f'A soma da sequência 3 é: {soma3}')



