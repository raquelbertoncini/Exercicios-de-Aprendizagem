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
    print(f'O log de {n} é {logaritmo:.2f}.')
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

print('14_ A nota final de um estudante é calculada a partir de 3 notas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das 3 notas mencionadas anteriormente obedece aos pesos: Trabalho de laboratório, 2; Avaliação Semestral, 3; Exame final, 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9), de recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.')
trab_laboratorio = float(input('Qual a nota do Trabalho de Laboratório? '))
av_semestral = float(input('Qual a nota da Avaliação Semestral? '))
exame_final = float(input('Qual a nota do Exame Final? '))
nota = (trab_laboratorio * 2) + (av_semestral * 3) + (exame_final * 5)
media = nota / 10
if media < 3:
    print(f'Sua média: {media:.2f}, você está reprovado.')
elif 3 <= media  <5:
    print(f'Sua média de {media:.2f} é suficiente para a recuperação.')
elif media >= 5:
    print(f'Parabéns! Você foi aprovado com média de {media:.2f}.')
print('-'*30)

print('15_ Usando switch, escreva um programa que leia um número inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda se 2 e assim por diante.')
dia = int(input('Digite um número entre 1 e 7:'))
if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-feira.')
elif dia == 3:
    print('Terça-feira')
elif dia == 4:
    print('Quarta-feira')
elif dia == 5:
    print('Quinta-feira')
elif dia == 6:
    print('Sexta-feira')
elif dia == 7:
    print('Sábado')
else:
    print('Você não digitou uma opção válida.')
print('-'*30)

print('16_ Usando switch, escreva um programa que leia um número inteiro entre 1 e 12 e imprima o mês correspondente.')
mes = int(input('Digite um número entre 1 e 12: '))
if mes == 1:
    print('Janeiro')
elif mes == 2:
    print('Fevereiro')
elif mes == 3:
    print('Março')
elif mes == 4:
    print('Abril')
elif mes == 5:
    print('Maio')
elif mes == 6:
    print('Junho')
elif mes == 7:
    print('Julho')
elif mes == 8:
    print('Agosto')
elif mes == 9:
    print('Setembro')
elif mes == 10:
    print('Outubro')
elif mes == 11:
    print('Novembro')
elif mes == 12:
    print('Dezembro')
else:
    print('Essa não é uma opção válida')
print('-'*30)

print('17_ Faça um programa que calcule e mostre a área de um trapézio.')
base_maior = 35
base_menor = 24
altura = 18
area = ((base_maior + base_menor) * altura) / 2
print(f'Base maior {base_maior}, base menor {base_menor}, altura {altura} este trapézio tem área total de {area}')
print('-'*30)

print('18_ Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas. O usuário escolhe uma das opções e o seu programa então pede 2 valores numéricos e realiza a operação, mostrando o resultado e saindo.')
print('Escolha a operação matemática que deseja realizar:')
operacao = input('Soma = S, Subtração = T, Adição = A, Multiplicação = M: ' ).upper()
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if operacao == 'S':
    soma = n1 + n2
    print(f'Realizando a soma de {n1} e {n2}, temos como resultado: {soma}.')
elif operacao == 'T':
    sub1 = n1 - n2
    sub2 = n2 - n1
    sub = max(n1,n2) - min(n1, n2)
    print(f'Subtraindo {n1} de {n2} temos: {sub1}.')
    print(f'Mas se for {n2} de {n1}, teremos {sub2}.')
    print(f'Mas se quiser a diferença do maior para o menor, o resultado é {sub}.')
print('-'*30)

print('19_ Faça um programa  para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas nao simultaneamente pelos dois.')
n = int(input('Digite seu número: '))
if n % 3 == 0 and not (n % 5 == 0):
    result = n / 3
    print(f'Resultado: {result}. É divisível por 3.')
elif n % 5 == 0 and not (n % 3 == 0):
    result = n / 5
    print(f'Resultado: {result}. É divisível por 5.')
else:
    print('e agora José?')
print('-'*30)

print('20_ Dados 3 valores, A B e C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um triângulo escaleno, equilátero ou isóscele considerando o seguinte: o comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados; chama-se equilátero o triângulo com 3 lados iguais; já o isósceles é aquele que tem o comprimento de dois lados iguais; recebe o nome de escaleno quando os 3 lados são difirentes.')
l1 = int(input('Digite o valor 1: '))
l2 = int(input('Digite o valor 2: '))
l3 = int(input('Digite o valor 3: '))
if l1 > (l2 + l3) or l2 > (l3 + l1) or l3 > (l2 + l1):
    print('Isso não é um triângulo.')
elif l1 == l2 == l3:
    print('É um triângulo equilátero.')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print('É um triângulo isósceles.')
elif l1 != l2 != l3:
    print('É um triângulo escaleno.')
print('-'*30)

print('21_ Escreva o menu de opções abaixo: Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.')
print('Escolha a opção:')
print('1 - Soma de 2 números.')
print('2 - Diferença entre 2 números (maior pelo menor).')
print('3 - Produto entre 2 números.')
print('4 - Divisão entre 2 números (o denominador não pode ser zero).')
opcao = int(input('OPÇÃO: '))
if opcao > 4:
    print('Você não digitou uma opção válida.')
elif opcao == 1:
    num1 = float(input('Qual o primeiro número? '))
    num2 = float(input('Qual o segundo número? '))
    print(num1 + num2)
elif opcao == 2:
    num1 = float(input('Qual o primeiro número? '))
    num2 = float(input('Qual o segundo número? '))   
    sub = max(num1, num2) - min(num1, num2)
    print(sub)
elif opcao == 3:
    num1 = float(input('Qual o primeiro número? '))
    num2 = float(input('Qual o segundo número? '))
    print(num1 * num2)
elif opcao == 4:
    num1 = float(input('Qual o primeiro número? '))
    num2 = float(input('Qual o segundo número? '))    
    if num2 == 0:
        print('o segundo número não pode ser zero.')
    else:
        print(num1 / num2)
print('-'*30)

print('22_ Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições de aposentadoria são: 1) ter pelo menos 65 anos; 2) ou ter trabalhado pelo menos 30 anos; 3) ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.)')
idade = int(input('Qual a sua idade? '))
tempo = int(input('Digite o tempo, em anos, trabalhado: '))
if 65 > idade >= 60 and tempo >= 25:
    print('Você pode se aposentar.')
elif tempo == 30:
    print('Você trabalho o tempo certo para ter a aposentaria concedida.')
elif idade >=65:
    print('Você tem a idade  para se aposentar.')
else:
    print('Você ainda nao pode se aposentar.')
    print('-'*30)

print('23_ Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e nao for divisível por 100. ')
# ano bissexto, é divisível por 4 mas não por 100 OU é divisível por 4, 100 e 400.
ano = int(input('Entre com o ano: '))
if ano % 4 == 0 and ano % 100!= 0:
    print('É ano bissexto.')
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('É ano bissexto.')
else:
    print('Não é ano bissexto.')
print('-'*30)

print('24_ Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma faixa diferente de imposto sobre o protudo - MG 7%, SP 12%, RJ 15%, MS 8%. Faça um programa em que o usuário entre o valor e o estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.')
valor = float(input('Qual o valor do produto? R$ '))
print('Minas Gerais = MG ;')
print('São Paulo = SP ;')
print('Rio de Janeiro = RJ ;')
print('Mato Grosso do Sul = MS .')
estado = input('Digite o estado de destino: ').upper()
if estado == 'MG':
    imposto = valor + (valor * 0.07)
    print(f'Seu produto de R$ {valor} tem valor de venda de R$ {imposto:.2f} em Minas Gerais.')
if estado == 'SP':
    imposto = valor + (valor * 0.12)
    print(f'Seu produto de R$ {valor} tem valor de venda de R$ {imposto:.2f} em São Paulo.')
if estado == 'RJ':
    imposto = valor + (valor * 0.15)
    print(f'Seu produto de R$ {valor} tem valor de venda de R$ {imposto:.2f} no Rio de Janeiro.')
if estado == 'MS':
    imposto = valor + (valor * 0.08)
    print(f'Seu produto de R$ {valor} tem valor de venda de R$ {imposto:.2f} em Mato Grosso do Sul.')
else:
    print('Esta não é uma opção válida.')
print('-'*30)

print('25_ ')
print('26_ Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo.')
print('consumo: menor que 8km/l - venda o carro')
print('consumo entre 8 e 12 km/l - econômico')
print('consumo maior que 13 km/l - super econômico.')
km = float(input('Digite a distância percorrida em km: '))
litro = float(input('Quantidade de litros de gasolina consumida: '))
consumo = km / litro
if consumo < 8:
    print(f'Seu carro faz {consumo:.2f}km/l, VENDA O CARRO!')
elif 8>= consumo <=12:
    print(f'Seu carro faz {consumo:.2f}km/l, ele é ECONÔMICO.')
elif consumo >=13:
    print(f'Seu carro é SUPER ECONÔMICO! Faz {consumo:.2f}km/l.')
print('-'*30)

print('27_ Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias.')
print('CATEGORIA INFANTIL A, INFANTIL B, JUVENIL A, JUVENIL B, SÊNIOR.')
print('IDADE: 5 A 7, 8 A 10, 11 A 13, 14 A 17, MAIORES DE 18 ANOS.')
idade = int(input('Digite a idade da pessoa nadadora: '))
if idade >= 5 and idade <=7:
    print('Você está na categoria INFANTIL A.')
elif idade >= 8 and idade <= 10:
    print('Você está na categoria  INFANTIL B.')
elif idade >= 11 and idade <= 13:
    print('Você está na categoria JUVENIL A.')
elif idade >= 14 and idade <= 17:
    print('Você está na categoria JUVENIL B.')
elif idade >= 18:
    print('Você já faz parte da categoria SÊNIOR.')
print('-'*30)

import math
print('28_ Faça um programa que leia 3 números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo com um valor numérico digitado pelo usuário.')
n1 = int(input('Digite o 1o número, de um total de 3: '))
n2 = int(input('Digite o 2o número, de um total de 3: '))
n3 = int(input('Digite o 3o número, de um total de 3: '))
print('(A) Média Geométrica \n'
       '(B) Média Ponderada \n'
       '(C) Média Harmônica \n'
       '(D) Média Aritmética')
opcao = input('Qual média deseja calcular? ').upper()
if opcao == 'A':
    r = n1 * n2 * n3
    r1 = math.pow(r, 1.0/3.0)
    print(f'A média geométrica é {r1:.2f}')
elif opcao == 'B':
    r = (n1 + 2 * n2 + 3 * n3) / 6
    print(f'A média ponderada é {r:.2f}')
elif opcao == 'C':
    r1 = (1/n1) + (1/n2) + (1/n3)
    r = 1 / r1
    print(f'A média harmônica é {r:.2f}')
elif opcao == 'D':
    r = (n1 + n2 + n3) / 3
    print(f'A média aritmética é {r:.2f}')
else:
    print('Essa não é uma opção válida.')
print('-'*30)


print("29_ Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: 'Qual a soma de a + b?' onde a e b são os números aleatórios. Peça a resposta, faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quantas vezes o aluno acertou.")
from random import randint

def soma(a, b):
    return a+ b

i = 0
acertos = 0
while i < 5:
    n1 = randint(0, 100)
    n2 = randint(0,100)
    print(n1, n2)
    r = int(input('Qual o resultado da soma dos números? '))
    i += 1
    if r == soma(n1, n2):
        acertos += 1
        print('Você acertou!')
    else:
        print('Não foi dessa vez.')
        print(f'O resultado é {soma(n1, n2)}')

print(f'Você acertou {acertos} perguntas!')
print('-'*30)

print('30_ Faça um programa que receba 3 números e mostre-os em ordem crescente.')
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))
n = [n1, n2, n3]
n.sort()
print(f'Seus números em ordem crescente: {n}.')
print('-'*30)
'''
print('31_ Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre qual a classificação dessa pessoa.')
