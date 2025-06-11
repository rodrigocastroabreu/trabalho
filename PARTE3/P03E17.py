#17) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

var_numero = int(input("Qual o número para calcular o fatorial?\n\t"));

var_fatorial = 1;
var_i = var_numero;
while var_i > 1:
    var_fatorial *= var_i;
    var_i -= 1;

print("O fatorial é:\n\t", var_fatorial);
