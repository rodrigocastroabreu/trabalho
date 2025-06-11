#24) Faça um programa que calcule o mostre a média aritmética de N notas.

var_qtd_notas = int(input("Qual qtd notas?\n\t"));

var_i = 1;
var_soma = 0;
while var_i <= var_qtd_notas:
    var_nota = float(input("Qual valor nota?\n\t"));
    var_soma += var_nota;
    var_i += 1;

var_media = (var_soma / var_qtd_notas);

print("A média é:\n\t", var_media);
