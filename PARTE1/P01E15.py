#15) Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros  quadrados da
#área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
#tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
#tinta a serem compradas e o preço total.

var_area = float(input("Qual o tamanho em metros quadrados da área a ser pintada?"));

var_litros = (var_area / 3);
var_qtd_latas = int(var_litros / 18);
var_preco_total = var_qtd_latas * 80;

print("Quantidades de latas de tinta a serem compradas é: ",var_qtd_latas);
print("O Preço total é: ",var_preco_total);
