'''print('1_ Faça um programa que receba dois números e mostre qual deles é o maior.')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
num = [n1, n2]
print(max(num))
print('-'*30)

import math
print('2_ Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada, se for negativo, mostre uma mensagem dizendo que o número é inválido.')
n = float(input('Digite um número: '))
if n < 0:
    print('Você não digitou um número válido!')
elif n > 0:
    n2 = math.sqrt(n)
    print(f'A raiz quadrada de {n} é {n2:.2f}')
print('-'*30)

print('3_ Leia um número real. Se o número for positivo imprima raiz quadrada. Do contrário, imprima o número ao quadrado.')
n1 = float(input('Digite um número: '))
import math
if n1 > 0:
    n2 = math.sqrt(n1)
    print(f'A raiz quadrada de {n1} é {n2:.2f}.')
elif n1 < 0:
    n2 = n1**2
    print(f'O quadrado de {n1} é {n2}.')
print('-'*30)

print('4_ Faça um programa que leia um número e, caso ele seja positivo, calcule o mostre: 1) o número digitado ao quadrado; 2) a raiz quadrada do número digitado.')
n = float(input('Digite um número: '))
from math import pow
if n < 0:
    print('Só estou aceitando números positivos. Operação encerrada.')
else:
    quadrado = n * n
    raiz = pow(n, 1/2)
    print(f'O quadrado de {n} é {quadrado}, e sua raiz quadrada é {raiz:.2f}.')
print('-'*30)

print('5_ Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.')
n = int(input('Qual é o seu número? '))
if n %2 == 0:
    print('Seu número é par!')
else:
    print('O número digitado é ímpar.')
print('-'*30)

print('6_ Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
maior = max(n1,n2)
diferenca = max(n1, n2) - min(n1,n2)
print(f'Dados os números {n1} e {n2}, o maior deles é o {maior}, a diferença entre os dois é {diferenca}.')
print('-'*30)

print('7_ Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem: números iguais.')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
maior = max(n1, n2)
if n1==n2:
    print('Eles são iguais!')
else:
    print(f'O maior número é: {maior}.')
print('-'*30)

print('8_ Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas (valor entre 0.0 e 10.0) e exiba na tela a média destas notas.')
print('Caso a nota não possua valor válido, este fato deve ser informado ao usuário, e o program termina.')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
if n1 > 10.0 or n1 < 0.0:
    print(f'Nota {n1} inválida.')
elif n2 > 10.0 or n2 < 0.0:
    print(f'Nota {n2} inválida.')
else:
    media = (n1 + n2) / 2
    print(f'A média das notas é {media}.')
print('-'*30)

print('9_ Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário, imprima: Empréstimo não concedido, caso contrário imprima Empréstimo concedido.')
salario = float(input('Qual é o seu salário: R$ '))
prestacao = float(input('Qual o valor da prestação: R$ '))
teto = salario * 0.2
if prestacao > teto:
    print('O empréstimo não pode ser concedido porque ultrapassa 20% do total.')
else:
    print('Empréstimo concedido.')
print('-'*30)

print('10_ Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre o seu peso ideal.')
sexo = input('Homem(h) ou mulher(m)? ').lower()
altura = float(input('Digite sua altura em metros: '))
if sexo == 'h':
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é de: {peso_ideal:.2f} kg.')
elif sexo == 'm':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é de {peso_ideal:.2f} kg.')
print('-'*30)

print('11_ Escreva um programa que leia um número inteiro maior do que zero e devolva, a soma de todos os seus algarismos.')
print('Se o número lido não for maior do que zero, o programa terminará com a mensagem: Número inválido.')
n = int(input('Digite um número: '))
soma = 0
if n > 0:
    for digit in str(n):
        soma += int(digit)
    print(soma)
else:
    print('Número inválido.')    
print('-'*30)

print('12_ Ler um número inteiro. Se o número lido for negativo, escreva a mensagem. "número inválido". Se o número for positivo, calcular o logaritmo dele.')
n = int(input('Digite um número:'))
import math
if n < 0:
    print('Número inválido.')
else:
    logaritmo = math.log(n)
    print(f'O log de {n} é {logaritmo:.2f}.)
print('-'*30)

print('13_ Faça um algoritmo que calcule a média ponderada das 3 notas de 3 provas. A 1a e a 2a tem peso1, a 3a tem peso 2. Ao final, mostrar a média do aluno e indicar se foi aprovado (igual ou superior a 60) ou reprovado.')
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
n3 = float(input('Insira a terceira nota: '))
nota = n1 + n2 + (n3 * 2)
media = nota / 4
if media >= 60:
    print(f'Sua média é de {media:.2f}, você foi aprovada.')
elif media <= 60:
    print(f'Sua média de {media:.2f} não foi suficiente. Você foi reprovada.')
print('-'*30)
'''
print('14_ A nota final de um estudante é calculada a partir de 3 notas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das 3 notas mencionadas anteriormente obedece aos pesos: Trabalho de laboratório, 2; Avaliação Semestral, 3; Exame final, 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9), de recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.')
