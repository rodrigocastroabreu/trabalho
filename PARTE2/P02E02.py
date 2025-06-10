#2) Faça um Programa que peça dois números e imprima o maior deles.

var_numero1 = float(input("Digite o primeiro número:\n"));
var_numero2 = float(input("Digite o segundo número:\n"));

if var_numero1 > var_numero2:
    print("O maior número é:\t", var_numero1);
elif var_numero2 > var_numero1:
    print("O maior número é:\t", var_numero2);
else:
    print("São números iguais");
