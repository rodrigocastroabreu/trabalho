#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
#área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a
#tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
# sempre arredonde os valores para cima, isto é, considere latas cheias.

var_area = float(input("Qual o tamanho em metros quadrados da área a ser pintada?\n "));

var_area = var_area * 1.1;
var_litros = var_area / 6;

var_qtd_latas = var_litros / 18;
var_preco_latas = var_qtd_latas * 80;

var_qtd_galoes = var_litros / 3.6;
var_preco_galoes = var_qtd_galoes * 25;

var_qtd_latas_misto = int(var_litros / 18);
var_restante = var_litros - (var_qtd_latas_misto * 18);
var_qtd_galoes_misto = var_restante / 3.6;
var_preco_misto = (var_qtd_latas_misto * 80) + (var_qtd_galoes_misto * 25);

print("Qtd de latas é: ", var_qtd_latas);
print("Preço total é: ", var_preco_latas);
print("Qtd de galões é: ", var_qtd_galoes);
print("O preço total é: ", var_preco_galoes);
print("Qtd Latas Misto: ", var_qtd_latas_misto);
print("Qtd Galões Misto: ", var_qtd_galoes_misto);
print("Preço total misto: ", var_preco_misto);
