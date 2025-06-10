#8) Faça um programa que leia 5 números e informe a soma e a média dos números.

var_numero1 = float(input("Qual primeiro número?\n\t"));
var_numero2 = float(input("Qual segundo número?\n\t"));
var_numero3 = float(input("Qual terceiro número?\n\t"));
var_numero4 = float(input("Qual quarto número?\n\t"));
var_numero5 = float(input("Qual quinto número?\n\t"));

var_soma = (var_numero1 + var_numero2 + var_numero3 + var_numero4 + var_numero5);
var_media = (var_soma / 5);

print("A soma é:\t", var_soma);
print("A média é:\t", var_media);
