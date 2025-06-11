#9) Faça um Programa que leia um vetor A com 10 números inteiros,
#calcule e mostre a soma dos quadrados dos elementos do vetor.

var_vetor = [];
var_soma_quadrados = 0;
var_i = 1;
while var_i <= 10:
    var_numero = int(input("Qual valor?\n\t"));
    var_vetor.append(var_numero);
    var_soma_quadrados += var_numero * var_numero;
    var_i += 1;

print("Soma dos quadrados:\n\t", var_soma_quadrados);
