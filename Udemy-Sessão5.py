print('1_ Faça um programa que receba dois números e mostre qual deles é o maior.')
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

print('31_ Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre qual a classificação dessa pessoa.')
altura = float(input('Digite a sua altura em metros: '))
peso = float(input('Qual o seu peso em kg? '))
if altura <= 1.20 and peso < 60:
        print('Classificação A')
elif altura <= 1.20 and 60 <= peso <= 90:
        print('Classificação D')
elif altura <=1.20 and  peso > 90:
        print('Classificação G')
elif 1.20 < altura <= 1.70 and peso < 60:
        print('Classificação B')
elif 1.20 < altura <= 1.70 and 60 <= peso <= 90:
        print('Classificação E')
elif 1.20 < altura <= 1.70 and peso > 90:
        print('Classificação H')
elif altura > 1.70 and peso < 60:
        print('Classificação C')
elif altura > 1.70 and 60 <= peso <= 90:
        print('Classificação F')
elif altura > 1.70 and peso > 90:
        print('Classificação I')
else:
        print('Ops, algo deu errado')
print('-'*30)

print('32_ Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão:\n'
'----------------------------------\n'
'Especificação  |  código  | preço\n'
'cachorro quente|   100    |  1.20\n'
'bauru simples  |   101    |  1.30\n'
'bauru com ovo  |   102    |  1.50\n'
'hamburguer     |   103    |  1.20\n'
'cheeseburguer  |   104    |  1.70\n'
'suco           |   105    |  2.20\n'
'refrigerante   |   106    |  1.00\n'
'----------------------------------')
codigo = int(input('Digite o código do pedido: '))
quanti = int(input('Qual a quantidade? '))
cardapio = {100: 'cachorro quente', 101: 'bauru simples', 102: 'bauru com ovo', 103:'hamburguer', 104: 'cheeseburguer', 105: 'suco', 106: 'refrigerante'}
preco = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20, 104: 1.70, 105: 2.20, 106: 1.00}
print(f' Você pediu {quanti} {cardapio[codigo]}, valor total de R$ {quanti * preco[codigo]}.')
print('-'*30)

print('33_ Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela).\n'
'______________________________________________________\n'
'PREÇO ANTIGO               |   PERCENTUAL DE AUMENTO\n'
'até R$ 50,00               |           5%\n'
'entre R$ 50,00 e R$ 100,00 |           10%\n'
'acima de R$ 100,00         |           15%\n'
'------------------------------------------------------\n'
'           PREÇO NOVO                 |    MENSAGEM\n'
'           até R$ 80,00               |  Barato\n'
'entre R$ 80,00 e R$ 120,00(inclusive) |  Normal\n'
'entre R$ 120,00 e R$ 200,00(inclusive |  Caro\n'
'         acima de R$ 200,00           |  Muito caro\n'
'------------------------------------------------------')
preco = float(input('Qual o preço do produto? R$ '))

def preco_novo(novo):
    if novo <= 80:
        return "Está barato"
    elif 80 < novo <= 120:
        return 'Está normal'
    elif 120 < novo <= 200:
        return 'Está caro'
    elif novo > 200:
        return 'Está muito caro'

if preco < 50:
    novo = preco + (preco * 0.05)
    print(f'O novo preço é {novo:.2f}')
    print(preco_novo(novo))

elif 50 <= preco < 100:
    novo = preco + (preco * 0.1)
    print(f'O novo preço é {novo:.2f}')
    print(preco_novo(novo))

elif preco >= 100:
    novo = preco + (preco * 0.15)
    print(f'O novo preço é {novo:.2f}')
    print(preco_novo(novo))
print('-'*30)

print('34_ Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela abaixo, quando o aluno tem mais e 20 faltas ocorre uma redução de conceito.\n'
'   NOTA           CONCEITO        CONCEITO\n'
'            (até 20 faltas) (mais de 20 faltas)\n'
'-----------------------------------------------\n'
'9.0 até 10.0       A               B\n'
'7.5 até 8.9        B               C\n'
'5.0 até 7.4        C               D\n'
'4.0 até 4.9        D               E\n'
'0.0 até 3.9        E               E')
nota = float(input('Digite a nota do aluno: '))
faltas = int(input('Quantidade de faltas: '))

if 0.0 < nota < 4.0:
    print('Conceito E')
elif 4 <=  nota < 5:
    if faltas <= 20:
        print('Conceito D')
    else:
        print('Conceito E')
elif 5 <=  nota < 7.5:
    if faltas <= 20:
        print('Conceito C')
    else:
        print('Conceito D')
elif 7.5 <=  nota < 9.0:
    if faltas <= 20:
        print('Conceito B')
    else:
        print('Conceito C')
elif 9 <=  nota <= 10.0:
    if faltas <= 20:
        print('Conceito A')
    else:
        print('Conceito B')
print('-'*30)

print('35_ Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês. Note que fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.')
print('-'*30)

print('36_ Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:\n'
'                   VENDA MENSAL                                    COMISSÃO\n'
'-------------------------------------------------------------------------------------\n'
'Maior ou igual a R$ 100.000,00                             R$ 700,00 + 16% das vendas\n'
'Menor que R$ 100.000,00 e maior ou igual a R$ 80.000,00    R$ 650,00 + 14% das vendas\n'
'Menor que R$ 80.000,00 e maior ou igual a R$ 60.000,00     R$ 600,00 + 14% das vendas\n'
'Menor que R% 60.000,00 e maior ou igual a R$ 40.000,00     R$ 550,00 + 14% das vendas\n'
'Menor que R$ 40.000,00 e maior ou igual a R$ 20.000,00     R$ 500,00 + 14% das vendas\n'
'Menor que R$ 20.000,00                                     R$ 400,00 + 14% das vendas\n'
'-------------------------------------------------------------------------------------')
venda = float(input('Digite o valor total das vendas: R$ '))

if venda >= 100000:
    p = venda * 0.16
    comissao = 700 + p
elif 80000 <= venda < 100000:
    p = venda * 0.14
    comissao = 650 + p
elif 60000 <= venda < 80000:
    p = venda * 0.14
    comissao = 600 + p
elif 40000 <= venda < 60000:
    p = venda * 0.14
    comissao = 550 + p
elif 20000 <= venda < 40000:
    p = venda * 0.14
    comissao = 500 + p
elif venda < 20000:
    p = venda * 0.14
    comissao = 400 + p

print(f' Valor total a receber de comissão: R$ {comissao:.2f}')
print('-'*30)

print('37_ As tarifas de certo parque de estacionamento são as seguintes:\n'
'1a e 2a hora       | R$ 1,00 cada\n'
'3a e 4a hora       | R$ 1,40 cada\n'
'5a hora e seguintes| R$ 2,00 cada\n'
'O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo de quem permanecer por 120 minutos. Os momentos de chegada ao parque e partida deste são apresentados na forma de pares de inteiros, representando horas e minutos. Por exemplo, o par 12 50 representará "dez para a uma da tarde". Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.')
print('-'*30)

print('38_ Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma data válida. Teste se o dia fornecido é um dia válido: dia > 0, dia <=28 para o mês de fevereiro (29 se o ano for bissexto), dia <=30 em abril, junho, setembro e novembro, dia <=31 nos outros meses. Teste a validade do mês: mês > 0 e mês <13. Teste a validade do ano: ano <= ano atual(use uma constante definida com o valor igual a 2008. Imprimir: "data válida" ou "data inválida" no final da execução do programa.')
dia = int(input('Digite o dia de nascimento: '))
mes = int(input('Digite o mês de nascimento: '))
ano = int(input('Digite o ano de nascimento: '))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    if 0 < dia <= 31:
        print('Data válida')
        idade = 2022 - ano
    else:
        print('Não é uma data válida')
    print(f'Você tem {idade} anos.')

elif mes in [4, 6, 9, 11]:
    if 0 < dia <= 30:
        print('Data válida')
        idade = 2022 - ano
    else:
        print('Não é uma data válida')
    print(f'Você tem {idade} anos.')

elif mes == 2:
    if 0 < dia <= 28:
        print('Data válida')
        idade = 2022 - ano
    elif dia == 29:
        print('Data válida! Ano bissexto')
    else:
        print('Não é uma data válida')
    print(f'Você tem {idade} anos.')
print('-'*30)

print('39_ Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente maior do que os funcionários com um salário maior, conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional de salário. Faça um programa que leia:\n'
'- o valor do salário atual do funcionário\n'
'- o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa)\n'
'Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.\n'
'_____________________________________________________________\n'
'SALÁRIO ATUAL      REAJUSTE    TEMPO DE SERVIÇO    BÔNUS\n'
'até 500,00             25%     abaixo de 1 ano     sem bônus\n'
'até 1000,00            20%     de 1 a 3 anos       100,00\n'
'até 1500,00            15%     de 4 a 6 anos       200,00\n'
'até 2000,00            10%     de 7 a 10 anos      300,00\n'
'acima de 2000,00   s/reajuste  mais de 10 anos     500,00\n'
'_____________________________________________________________')
salario = float(input('Digite o salário atual: R$ '))
tempo = int(input('Qual o tempo de serviço(em anos): '))

def bonus(tempo):
    if 1 <= tempo <= 3:
        return(f'Você tem direito a R$ 100,00 de bônus pelos seus {tempo} anos de trabalho.')
    elif 4 <= tempo <= 6:
        return(f'Você tem direito a R$ 200,00 de bônus pelos seus {tempo} anos de trabalho.')
    elif 7 <= tempo <= 10:
        return(f'Você tem direito a R$ 300,00 de bônus pelos seus {tempo} anos de trabalho.')
    elif tempo > 10:
        return(f'Você tem direito a R$ 500,00 de bônus pelos seus {tempo} anos de trabalho.')
    else:
        return('Você não tem direito ao bônus.')

if salario <= 500.00:
    r = salario * 0.25
    novo = salario + r
    print(f'Reajuste de R$ {r:.2f}, seu novo salário R$ {novo:.2f}')
    print(bonus(tempo))

elif salario <= 1000.00:
    r = salario * 0.20
    novo = salario + r
    print(f'Reajuste de R$ {r:.2f}, seu novo salário R$ {novo:.2f}')
    print(bonus(tempo))

elif salario <= 1500.00:
    r = salario * 0.15
    novo = salario + r
    print(f'Reajuste de R$ {r:.2f}, seu novo salário R$ {novo:.2f}')
    print(bonus(tempo))

elif salario <= 2000.00:
    r = salario * 0.10
    novo = salario + r
    print(f'Reajuste de R$ {r:.2f}, seu novo salário R$ {novo:.2f}')
    print(bonus(tempo))

elif salario > 2000.00:
    print('Você não tem direito ao reajuste.')
    print(bonus(tempo))

print('-'*30)

print('40_ O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.')
print('CUSTO DE FÁBRICA                      % DO DISTRIBUIDOR      % DOS IMPOSTOS\n'
'até R$ 12.000,00                               5                   isento\n'
'entre R$ 12.000,00 e R$ 25.000,00              10                  15\n'
'acima de R$ 25.000,00                          15                  20')
custo = float(input('Qual o custo de fábrica do veículo? R$ '))

if custo <= 12000:
    comissao = custo * 0.05
    venda = custo + comissao
    print(f'Isento de impostos. Custo ao consumidor: R$ {venda:.2f}')

elif 12000 < custo <= 25000:
    comissao = custo * 0.10
    imposto = custo * 0.15
    venda = custo + comissao + imposto
    print(f'Imposto: R$ {imposto:.2f},\nComissão: R$ {comissao:.2f},\nCusto ao consumidor: R$ {venda:.2f}')

elif custo > 25000:
    comissao = custo * 0.15
    imposto = custo * 0.20
    venda = custo + comissao + imposto
    print(f'Imposto: R$ {imposto:.2f},\nComissão: R$ {comissao:.2f},\nCusto ao consumidor: R$ {venda:.2f}')
else:
    print('Aqui podemos ver algum retorno de erro do Python')
print('-'*30)

print('41_ Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:\n'
'IMC            CLASSIFICAÇÃO\n'
'< 18,5         Abaixo do peso\n'
'18.6 - 24.9    Saudável\n'
'25.0 - 29.9    Peso em excesso\n'
'30.0 - 34.9    Obesidade grau I\n'
'35.0 - 39.9    Obesidade grau II (severa)\n'
'>= 40.0        Obesidade grau III (mórbida)')
peso = float(input('Digite o peso em kg: '))
alt = float(input('Digite a altura em metros: '))
imc = peso / (alt  **2)
if imc < 18.5:
    print(f'{imc:.2f}')
    print('Abaixo do peso')
elif 18.6 <=imc <= 24.9:
    print(f'{imc:.2f}')
    print('Saudável')
elif 25.0 <= imc <= 29.9:
    print(f'{imc:.2f}')
    print('Peso em excesso')  
elif 30.0 <= imc <= 34.9:
    print(f'{imc:.2f}')
    print('Obesidade grau I')
elif 35.0 <= imc <= 39.9:
    print(f'{imc:.2f}')
    print('Obesidade grau II(severa)')
elif imc >= 40.0:
    print(f'{imc:.2f}')
    print('Obesidade grau III(mórbida)')