print('Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0')
contador = 0
for i in range (1,1000):
    if contador >= 5:
        break

    if i % 3 == 0:
        print(i)
        contador += 1
