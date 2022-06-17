'''print('1_ Faça um programa que leia um número inteiro e o imprima.')
n = 10
print(n)
print('- '*30)

print('2_ Faça um programa que leia um número real e o imprima.')
n = -15
print(n)
print('- '*30)

print('3_ Peça ao usuário para digitar 3 valores inteiros e imprima a soma deles.')
n1 = int(input('Digite 1o número: '))
n2 = int(input('Digite 2o número: '))
n3 = int(input('Digite 3o número: '))
soma = n1 + n2 + n3
print(f'A soma dos 3 números é: {soma}.')
print('- '*30)

print('4_ Leia um número real e imprima o resultado do quadrado desse número.')
n = 20
square = n * n
print(square) 
print('- '*30)

print('5_ Leia um número real e imprima a quinta parte deste número.')
n = 25
part5 = n /5
print(part5)
print('_ '*30)

print('6_ Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit')
celsius = 37
convertF = celsius * (9 / 5) + 32
print(f'{celsius} graus Celsius equivalem a {convertF:.2f} graus Fahrenheit.')
print('- '*30) 

print('7_ Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.')
fahren = 98.60
convertC = 5 * (fahren - 32) / 9
print(f'{fahren} graus Fahrenheit equivalem a {convertC} graus Celsius')
print('- '*30)

print('8_ Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius')
kelvin = 350
celsius = kelvin - 273.15
print(f'{kelvin} graus kelvin é igual a {celsius:.2f} graus celsius.')
print('- '*30)

print('9_ Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.')
celsius = 76.85
kelvin = celsius + 273.15
print(f'{celsius} graus Celsius são {kelvin} graus Kelvin.')
print('- '*30)

print('10_ Leia uma velocidade em km/h e apresente-a convertida em m/s.')
km = 250
metros = km / 3.6
print (f'{km} km/h')
print(f'É o mesmo que {metros:.2f} m/s.')
print('- '*30)

print('11_ Leia uma velocidade em m/s e apresente-a em km/h.')
metros = 70
km = metros * 3.6
print(f'{metros} m/s são {km} km/h.')
print('- '*30)
'''
print('12_ Leia uma distância em milhas e apresente-a convertida em quilômetros.')
milhas = 300
km = 1.61 * milhas
print(f'{milhas} milhas, são {km:.2f} quilômetros.')
print('- '*30)

print('13_ Leia uma distância em quilômetros e apresente-a convertida em milhas.')
km = 480
milhas = km / 1.61
print(km, 'km')
print(f'São {milhas:.2f} milhas.')
