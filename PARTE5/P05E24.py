#24) Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os
#resultados em um vetor .
# Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random;

var_resultados = [];
var_contadores = [0, 0, 0, 0, 0, 0];
var_i = 1;

while var_i <= 100:
    var_numero = random.randint(1, 6);
    var_resultados.append(var_numero);
    var_contadores[var_numero - 1] += 1;
    var_i += 1;

print("Resultados:\n\t", var_resultados);
print("Qtd cada número:\n\t");
var_i = 0;
while var_i < 6:
    print(var_i + 1, ":", var_contadores[var_i]);
    var_i += 1;
