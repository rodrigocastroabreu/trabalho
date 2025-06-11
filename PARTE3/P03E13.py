#13) Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado
#ao segundo número. Não utilize a função de potência da linguagem.

var_base = int(input("Qual o número base?\n\t"));
var_expoente = int(input("Qual o expoente?\n\t"));

var_i = 0;
var_resultado = 1;
while var_i < var_expoente:
    var_resultado *= var_base;
    var_i += 1;

print("O resultado da potência é:\n\t", var_resultado);
