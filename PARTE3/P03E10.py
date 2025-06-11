#10) Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
#compreendido por eles.

var_numero1 = int(input("Qual primeiro número?\n\t"));
var_numero2 = int(input("Qual segundo número?\n\t"));

var_menor = min(var_numero1, var_numero2);
var_maior = max(var_numero1, var_numero2);

print("O intervalo compreendido por eles é:\n\t");

var_i = var_menor + 1;
while var_i < var_maior:
    print("\n\t", var_i);
    var_i += 1;
