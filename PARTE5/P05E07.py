#7) Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

var_vetor = [];
var_soma = 0;
var_multiplicacao = 1;
var_i = 1;
while var_i <= 5:
    var_numero = int(input("Qual valor?\n\t"));
    var_vetor.append(var_numero);
    var_soma += var_numero;
    var_multiplicacao *= var_numero;
    var_i += 1;

print("Números:\n\t", var_vetor);
print("Soma:\n\t", var_soma);
print("Multiplicação:\n\t", var_multiplicacao);
