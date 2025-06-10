#14) Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda,
#etc.), se digitar outro valor deve aparecer valor inválido.

var_numero = int(input("Qual valor de 1 a 7 para ver dia correspondente da semana?\n\t"));

var_dias = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

if var_numero in var_dias:
    print("O dia da semana é:\n\t", var_dias[var_numero]);
else:
    print("Valor inválido!\n\t");
