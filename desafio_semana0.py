"""
Faça um programa que Calcule a soma de três números inteiros. O programa deve exibir na tela uma mensagem como a indicada abaixo de exemplo:
"""
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: ')) 


def calculo(a, b, c):
    soma = a + b + c

    print(f'Entrada: {a}, {b}, {c}')
    print(f'Processamento: {a} + {b} + {c}')
    print(f'Saída: {soma}')

calculo(num1, num2, num3)
