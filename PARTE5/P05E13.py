#13) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

var_temperaturas = [];
var_i = 1;
while var_i <= 12:
    print("Mês", var_i, ":");
    var_temperaturas.append(float(input("Qual valor?\n\t")));
    var_i += 1;

var_soma = 0;
var_i = 0;
while var_i < 12:
    var_soma += var_temperaturas[var_i];
    var_i += 1;
var_media = (var_soma / 12);

print("Média:\n\t",var_media);
var_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

var_i = 0;
while var_i < 12:
    if var_temperaturas[var_i] > var_media:
        print(var_meses[var_i], ":", var_temperaturas[var_i]);
    var_i += 1;
