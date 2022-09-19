print('Faça um programa que some os números ímpares obtidos em um intervalo definido pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo, e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior do que o valor final) deve ser escrito uma mensagem de erro na tela "Intervalo de valores inválido" e o programa termina.')
n1 = int(input("Digite o valor de início: "))
n2 = int(input('Digite o valor de parada (deve ser maior do que o inicial): '))

soma = 0

if n1 < n2:

    for i in range(n1, n2 +1):
       
        if i % 2 == 1:
            soma += i
            
    print(f'A soma do intervalo é: {soma}   ')

else:
    print('Intervalo de valores inválido.')


