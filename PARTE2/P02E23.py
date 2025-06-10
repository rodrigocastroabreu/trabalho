#23) Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador
#módulo (resto da divisão).

var_numero = int(input("Qual o número inteiro?\n\t"));

if var_numero % 2 == 0:
    print("O número é par\n\t", var_numero);
else:
    print("O número é ímpar\n\t", var_numero);
