print('* '*30)
print('Lista de exercícios do 1 ao 20.')
print('* '*30)
import time
time.sleep(3)

print('1_ Faça um programa que leia um número inteiro e o imprima.')
n = 10
print(n)
print('- '*30)
time.sleep(3)

print('2_ Faça um programa que leia um número real e o imprima.')
n = -15
print(n)
print('- '*30)
time.sleep(3)

print('3_ Peça ao usuário para digitar 3 valores inteiros e imprima a soma deles.')
n1 = int(input('Digite 1o número: '))
n2 = int(input('Digite 2o número: '))
n3 = int(input('Digite 3o número: '))
soma = n1 + n2 + n3
print(f'A soma dos 3 números é: {soma}.')
print('- '*30)
time.sleep(3)

print('4_ Leia um número real e imprima o resultado do quadrado desse número.')
n = 20
square = n * n
print(square) 
print('- '*30)
time.sleep(5)
print('5_ Leia um número real e imprima a quinta parte deste número.')
n = 25
part5 = n /5
print(part5)
print('_ '*30)
time.sleep(5)

print('6_ Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit')
celsius = 37
convertF = celsius * (9 / 5) + 32
print(f'{celsius} graus Celsius equivalem a {convertF:.2f} graus Fahrenheit.')
print('- '*30) 
time.sleep(5)

print('7_ Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.')
fahren = 98.60
convertC = 5 * (fahren - 32) / 9
print(f'{fahren} graus Fahrenheit equivalem a {convertC} graus Celsius')
print('- '*30)
time.sleep(5)

print('8_ Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius')
kelvin = 350
celsius = kelvin - 273.15
print(f'{kelvin} graus kelvin é igual a {celsius:.2f} graus celsius.')
print('- '*30)
time.sleep(5)

print('9_ Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.')
celsius = 76.85
kelvin = celsius + 273.15
print(f'{celsius} graus Celsius são {kelvin} graus Kelvin.')
print('- '*30)
time.sleep(5)

print('10_ Leia uma velocidade em km/h e apresente-a convertida em m/s.')
km = 250
metros = km / 3.6
print (f'{km} km/h')
print(f'É o mesmo que {metros:.2f} m/s.')
print('- '*30)
time.sleep(5)

print('11_ Leia uma velocidade em m/s e apresente-a em km/h.')
metros = 70
km = metros * 3.6
print(f'{metros} m/s são {km} km/h.')
print('- '*30)
time.sleep(5)

print('12_ Leia uma distância em milhas e apresente-a convertida em quilômetros.')
milhas = 300
km = 1.61 * milhas
print(f'{milhas} milhas, são {km:.2f} quilômetros.')
print('- '*30)
time.sleep(5)

print('13_ Leia uma distância em quilômetros e apresente-a convertida em milhas.')
km = 480
milhas = km / 1.61
print(km, 'km')
print(f'São {milhas:.2f} milhas.')
print('- '*30)
time.sleep(5)

print('14_ Leia um ângulo em graus e apresente-o convertido em radianos.')
graus = 345
radianos = graus * (3.14/180)
print(graus, 'graus')
print(f'Equivalem a {radianos:.2f} graus radianos')
print('- '*30)
time.sleep(5)

print('15_ Leia um ângulo em radianos e apresente-o convertido em graus')
radiano = 6
grau = radiano * (180/3.14)
print(f'{radiano} graus radianos equivalem a {grau:.2f} graus.')
print('- '*30)
time.sleep(5)

print('16_ Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.')
polegada = 120
centimetro = polegada * 2.54
print(f'{polegada} " (polegadas) são {centimetro} centímetros.')
print('- '*30)
time.sleep(5)

print('17_ Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas')
cm = 298
pol = cm / 2.54
print(f'{cm} centímetros são {pol:.2f} polegadas.')
print('- '*30)
time.sleep(5)

print('18_ Leia um valor de volume em metros cúbicos e apresente-o convertido em litros.')
metros3 = 3580
litros = 1000 * metros3
print(f'{metros3} m3.')
print(f'equivalem a {litros} litros.')
print('- '*30)
time.sleep(5)

print('19_ Leia um valor de volume em litros e apresente-o convertido em metros cúbicos.')
litros = 3580000
metros3 = litros / 1000
print(f'{litros} litros são {metros3} m3.')
print('- '*30)
time.sleep(5)

print('20_ Leia um valor de massa em quilogramas e apresente-o convertido em libras.')
kg = 84
libra = kg / 0.45
print(f'Um peso de {kg} kg é o mesmo que {libra:.2f} libras.')
