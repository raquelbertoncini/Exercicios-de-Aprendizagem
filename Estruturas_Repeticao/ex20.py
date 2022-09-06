print('Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados lidos e  número de valores pares. O processo termina quando for digitado o número 1000.')
n = 0
count = 0
lista = []
listapar = []
while n != 1000:
    n = int(input('Digite um número: '))
    lista.append(n)
    count += 1
    if n % 2 == 0:
        listapar.append(n)

pares = len(listapar)
print(f'Foram lidos {count} números, dos quais {pares} são pares: {listapar}')
