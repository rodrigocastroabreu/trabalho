#3) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

var_notas = [];
var_i = 1;
var_soma = 0;
while var_i <= 4:
    var_nota = float(input("Qual nota?\n\t"));
    var_notas.append(var_nota);
    var_soma += var_nota;
    var_i += 1;

var_media = (var_soma / 4);

print("Notas:\n\t", var_notas);
print("Média:\n\t", var_media);
