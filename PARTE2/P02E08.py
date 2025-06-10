#8) Faça um Programa que leia três números e mostre o maior e o menor deles.

var_numero1 = float(input("Valor do primeiro número:\n\t"));
var_numero2 = float(input("Valor do segundo número:\n\t"));
var_numero3 = float(input("Valor do terceiro número:\n\t"));

if var_numero1 > var_numero2 and var_numero1 > var_numero3:
    var_maior = var_numero1;
elif var_numero2 > var_numero1 and var_numero2 > var_numero3:
    var_maior = var_numero2;
else:
    var_maior = var_numero3;

if var_numero1 < var_numero2 and var_numero1 < var_numero3:
    var_menor = var_numero1;
elif var_numero2 < var_numero1 and var_numero2 < var_numero3:
    var_menor = var_numero2;
else:
    var_menor = var_numero3;

print("O maior número é:\n\t", var_maior);
print("O menor número é:\n\t", var_menor);
