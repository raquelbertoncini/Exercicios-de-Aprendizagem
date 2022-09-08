print('Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de notas (válidas no intervalo de 10 a 20) e mostre na tela, como resultado, a correspondente média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação.')
soma = 0
quant = 0

while True:
    nota = float(input('Digite a nota entre 10 e 20: '))

    if 10 <= nota <= 20:
        soma += nota
        quant += 1

    else:
        print('Nota inválida.')
        break

media = soma / quant
print(f'A média das notas válidas inseridas é {media:.2f}')