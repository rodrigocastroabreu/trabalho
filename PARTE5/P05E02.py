#2) Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

var_vetor = [];
var_i = 1;
while var_i <= 10:
    var_numero = float(input("Qual valor?\n\t"));
    var_vetor.append(var_numero);
    var_i += 1;

var_i = 9;
print("Ordem inversa:\n\t");
while var_i >= 0:
    print("\t", var_vetor[var_i]);
    var_i -= 1;
