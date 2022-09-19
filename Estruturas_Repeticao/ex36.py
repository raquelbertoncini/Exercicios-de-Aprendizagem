print('Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 10 números naturais e o quadrado da soma.')
soma_quadrado = 0
quadrado_soma = 0
soma_n = 0
for i in range(1, 11):
    quadrado = i * i
    soma_quadrado += quadrado
    soma_n += i
    quadrado_soma = soma_n * soma_n
    

print(f' A soma dos quadrados dos 10 primeiros números é: {soma_quadrado},\n'
f'enquanto o quadrado da soma é {quadrado_soma},\n'
f'e , a diferença entre eles é: {quadrado_soma - soma_quadrado}.')