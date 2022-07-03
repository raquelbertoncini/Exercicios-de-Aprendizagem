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
'''