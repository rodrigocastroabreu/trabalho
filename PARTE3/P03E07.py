#7) Faça um programa que leia 5 números e informe o maior número.

var_numero1 = float(input("Qual primeiro número?\n\t"));
var_numero2 = float(input("Qual segundo número?\n\t"));
var_numero3 = float(input("Qual terceiro número?\n\t"));
var_numero4 = float(input("Qual quarto número?\n\t"));
var_numero5 = float(input("Qual quinto número?\n\t"));

var_maior_numero = max(var_numero1, var_numero2, var_numero3, var_numero4, var_numero5);

print("O maior número é:\n\t", var_maior_numero);

