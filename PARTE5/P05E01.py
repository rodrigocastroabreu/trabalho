#1) Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

var_vetor = [];
var_i = 1;
while var_i <= 5:
    var_numero = int(input("Qual valor?\n\t"));
    var_vetor.append(var_numero);
    var_i += 1;

print("O vetor é:\n\t", var_vetor);
