#3) Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

var_valor = float(input("Digite um valor:\n"));

if var_valor > 0:
    print("O valor é positivo.");
elif var_valor < 0:
    print("O valor é negativo.");
else:
    print("O valor é zero.");
