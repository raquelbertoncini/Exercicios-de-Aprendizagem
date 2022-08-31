print('Escreva um programa que escreva na tela, de 1 a 100, de 1 em 1, 3 vezes. A primeira vez deve usar a estrutura de repetição for, a segunda while, e a terceira do while')

'''Como fazer um do while em Python?
Ao final do while podemos utilizar a instrução else. O propósito disso é executar alguma instrução ou bloco de código ao final do loop, como podemos ver no exemplo a seguir: contador = 0 while (contador < 5): print(contador) contador = contador + 1 else: print("O loop while foi encerrado com sucesso!")'''
print('utilizando for')
contador = 0
for i in range (1, 101):
    print (i)

print('utilizando while')
i = 0
while i <=100:
    print(i)
    i += 1
