#10) Faça um Programa que leia três números e mostre-os em ordem decrescente.

var_numero1 = float(input("Qual o primeiro número?\n\t"));
var_numero2 = float(input("Qual o segundo número?\n\t"));
var_numero3 = float(input("Qual o terceiro número?\n\t"));

if var_numero1 >= var_numero2 and var_numero1 >= var_numero3:
    if var_numero2 >= var_numero3:
        print("Ordem decrescente:\n\t", var_numero1, var_numero2, var_numero3);
    else:
        print("Ordem decrescente:\n\t", var_numero1, var_numero3, var_numero2);
elif var_numero2 >= var_numero1 and var_numero2 >= var_numero3:
    if var_numero1 >= var_numero3:
        print("Ordem decrescente:\n\t", var_numero2, var_numero1, var_numero3);
    else:
        print("Ordem decrescente:\n\t", var_numero2, var_numero3, var_numero1);
else:
    if var_numero1 >= var_numero2:
        print("Ordem decrescente:\n\t", var_numero3, var_numero1, var_numero2);
    else:
        print("Ordem decrescente:\n\t", var_numero3, var_numero2, var_numero1);

