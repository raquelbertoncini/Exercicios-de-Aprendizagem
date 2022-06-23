print('*'*30)
print('21_ Leia um valor de massa em libras e apresente-o convertido em quilogramas.')
libra = 160
quilo = libra * 0.45
print(f' {libra} libras são {quilo} kg.')
print('*'*30)
import time
time.sleep(4)

print('22_ Leia um valor de comprimento em jardas e apresente-o convertido em metros.')
jardas = 800
metro = 0.91 * jardas
print(f'{jardas} jardas equilavem a {metro} metros.')
print('*'*30)
time.sleep(4)

print('23_ Leia um valor de comprimento em metros e apresente-o convertido em jardas.')
metro = 728
jardas = metro / 0.91
print(f'Tirando a prova... {metro} metros são {jardas} jardas.')
print('*'*30)
time.sleep(4)

print('24_ Leia um valor de área em metros quadrados e apresente-o convertido em acres.')
m2 = 400
acre = m2 * 0.000247
print(f'{m2} m2 = {acre} acres.')
print('*'*30)
time.sleep(4)

print('25_ Leia um valor de área em acres e apresente-o convertido em metros quadrados')
acre = 4
m2 = acre * 4048.58
print(f'{acre} acres são {m2} metros quadrados.')
print('*'*30)
time.sleep(4)

print('26_ Leia um valor de área em metros quadrados e apresente-o convertido em hectares.')
m2 = 3000
hectare = m2 * 0.0001
print(m2, 'metros quadrados')
print(f'é o mesmo que {hectare} hectares.')
print('*'*30)
time.sleep(4)

print('27_ Leia um valor de área em hectares e apresente-o convertido em metros quadrados')
hect = 5
metro = hect * 10000
print(hect, 'hectares')
print(metro, 'metros quadrados')
print('*'*30)
time.sleep(4)

print('28_ Faça a leitura de 3 valores e apresente como resultado a soma dos quadrados dos 3 valores lidos.')
v1 = 20
v2 = 39
v3 = 51
resultado = (v1 ** 2) + (v2 ** 2) + (v3 ** 2)
print (v1, v2, v3)
print(f'A soma dos quadrados dos números apresentados é {resultado}.')
print('*'*30)
time.sleep(4)

print('29_ Leia quatro notas, calcule a média aritmética e imprima o resultado.')
n1 = 6
n2 = 9
n3 = 7
n4 = 10
media = (n1 + n2 + n3 + n4)/ 4
print(n1, n2, n3, n4)
print(f'Média aritmética = {media}.')
print('*'*30)
time.sleep(4)

print('30_ Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.')
real = 450
cotacao = 5.19
dolar = real * cotacao
print(f' R$ {real} reais são {dolar:.2f} dólares no dia de hoje, 23 de junho de 2022.')
print('*'*30)
time.sleep(4)

print('31_Leia um número inteiro e imprima o seu antecessor e o seu sucessor.')
n = 34
antes = n - 1
depois = n + 1
print(f'Número: {n}, antecessor: {antes}, sucessor {depois}')
print('*'*30)
time.sleep(4)

print('32_Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor do seu dobro.')
n = 25
triplo = n * 3
dobro = n * 2
resultado = (triplo + 1) + (dobro - 1)
print(f'número: {n}, resultado: {resultado}.')
print('*'*30)
time.sleep(4)

print('33_Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.')
lado = 12
area = lado * lado
print(f'Um quadrado de lado {lado}, tem área total de {area}.')
print('*'*30)
time.sleep(4)

print('34_Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.')
raio = 120
area = 3.141592 * (raio ** 2)
print(f'um círculo com raio de {raio} tem área total de {area:.2f}.')
print('*'*30)
time.sleep(4)

print('35_Sejam a e b os catetos de um triângulo. Faça um programa que receba os valores, de a e b e calcule o valor da hipotenusa. Imprima o resultado dessa operação.')
a = 6
b = 5
import math
hipo = math.sqrt((a **2) + (b **2))
print(f'catetos {a, b} e hipotenusa calculada: {hipo:.2f}')
print('*'*30)
time.sleep(4)

print('36_Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.')
altura = 10
raio = 8
volume = 3.141592 * (raio ** 2) * altura 
print(f'Cilindro circular com altura {altura}, raio = {raio} tem volume final de {volume:.2f}.')
print('*'*30)
time.sleep(4)

print('37_Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.')
value = 2550
discount = 0.12
final = value - (value * discount)
print(f'Um produto com valor de R$ {value}, com desconto de 12% tem valor final de {final:.2f}.')
print('*'*30)
time.sleep(4)

print('38_Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.')
salario = 1300
turbinado = salario + (salario * 0.25)
print(f'Parabéns! Seu salário de {salario} foi turbinado em 25% e você receberá {turbinado:.2f} reais a partir de agora.')
print('*'*30)
time.sleep(4)

print('39_ A importância de R$ 780.000,00 será dividida entre 3 ganhadores de um concurso. Sendo que da quanti total:')
print('O primeiro ganhador receberá 46%;')
print('O segundo receberá 32%;')
print('O terceiro receberá o restante.')
print('Calcule e imprima a quantia ganha por cada um dos ganhadores.')
n = 780000
n1 = n * 0.46
n2 = n * 0.32
n3 = n * 0.22
print(f'1o ganhador: {n1}, 2o ganhador: {n2} e 3o ganhador {n3}')
print('*'*30)
time.sleep(4)

print('40_Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.')
valordia = 120
totaldias = int(input('\033[0;31;107mDigite o total de dias trabalhados:\033[m'))
valorbruto = totaldias * valordia
liquido = valorbruto - (valorbruto * 0.08)
print(f'Já que o encanador trabalhou por {totaldias} dias, sendo R$ {valordia} a diária, receberia R$ {valorbruto:.2f} mas há o desconto de 8% do IR, sendo que o líquido recebido será de R$ {liquido:.2f}.')
