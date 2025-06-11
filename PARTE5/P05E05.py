#5) Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.

var_vetor = [];
var_par = [];
var_impar = [];
var_i = 1;
while var_i <= 20:
    var_numero = int(input("Qual valor?\n\t"));
    var_vetor.append(var_numero);

    if var_numero % 2 == 0:
        var_par.append(var_numero);
    else:
        var_impar.append(var_numero);

    var_i += 1;

print("Vetor:\n\t", var_vetor);
print("Vetor PAR:\n\t", var_par);
print("Vetor ÍMPARES:\n\t", var_impar);
