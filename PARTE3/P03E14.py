#14) Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
#quantidade de números impares.

var_pares = 0;
var_impares = 0;

var_i = 1;
while var_i <= 10:
    var_numero = int(input("Qual número?\n\t"));

    if var_numero % 2 == 0:
        var_pares += 1;
    else:
        var_impares += 1;

    var_i += 1;

print("A qtd de pares é:\n\t", var_pares);
print("A qtd de ímpares é:\n\t", var_impares);
