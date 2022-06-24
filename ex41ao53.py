'''print('*'*30)
print('41_ Faça um programa que leia o valor da hora de trabalho e  número de horas trbalhadas no mês. Imprima o valoro a ser pago ao funcionário, adicionando 10% sobre o valor calculado.')
valorhora = 80
horas = 160
valorbruto = valorhora * horas
valorliquido = valorbruto + (valorbruto * 0.10)
print(f'O funcionário trabalhou {horas} horas no mês, o combinado é de R$ {valorhora} por hora, o que lhe dá direito a R$ {valorbruto:.2f}, somando o adicional de 10%, no total são R$ {valorliquido:.2f}.')
print('*'*30)

print('42_ Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.')
salario = float(input('\033[33;43mQual é o seu salário-base?\033[m R$ '))
bonus = salario * 0.05
imposto = salario * 0.07
print(f'Gratificação: R$ {bonus:.2f}')
print(f'IR : R$ {imposto:.2f}')
print(f'Salário líquido a receber: R$ {salario + bonus - imposto}')
print('*'*30)

print('43_ Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:')
print('- o total a pagar com desconto de 10%') 
print('- o valor de cada parcela, no parcelamento em 3x sem juros')
print('- a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)')
print('- a comissão do vendedor, no caso da venda parcelada (5% sobre o valor total)')
venda = float(input('\033[33mQual o valor total dos produtos:\033[m R$ '))
tipovenda = input('Venda à vista (V) ou a prazo (P)? ').upper()
if tipovenda == 'V':
    total = venda - (venda * 0.1)
    comissao = total * 0.05
    print(f'O valor final, com desconto de 10%, é de R$ {total:.2f}')
    print(f'A comissão do vendedor é de R$ {comissao:.2f}')
elif tipovenda == 'P':
    parcela = venda / 3
    comissao = venda * 0.05
    print(f'O pagamento será feito em 3 parcelas de R$ {parcela:.2f} cada')
    print(f'A comissão do vendedor é de R$ {comissao:.2f}')
else:
    print('Digite uma opção válida')
print('*'*30)

#pesquisar como arredondar para cima
print('44_ Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.')
altura = float(input('\033[33mQual a altura do degrau, em cm?\033[m '))
objetivo = float(input('\033[33mQual a altura que deseja alcançar com a escada, em metros?\033[m '))
obj = objetivo * 100
degrau = obj / altura
print(f'Você precisará subir {degrau} degraus para atingir seu objetivo.')
'''
print('45_ Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASCII para resolver o problema.')
