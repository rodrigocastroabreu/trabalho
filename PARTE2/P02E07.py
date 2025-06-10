#7) Faça um Programa que leia três números e mostre o maior deles.

var_numero1 = float(input("Digite o primeiro número:\n\t"));
var_numero2 = float(input("Digite o segundo número:\n\t"));
var_numero3 = float(input("Digite o terceiro número:\n\t"));

if var_numero1 > var_numero2 and var_numero1 > var_numero3:
    print("O maior número é:\n\t", var_numero1);
elif var_numero2 > var_numero1 and var_numero2 > var_numero3:
    print("O maior número é:\n\t", var_numero2);
elif var_numero3 > var_numero1 and var_numero3 > var_numero2:
    print("O maior número é:\n\t", var_numero3);
else:
    print("Os números são iguais ou tem valores repetidos\n\t");
