#18) Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se
#este ano é ou não bissexto.

var_ano = int(input("Qual ano verificar se é bissexto?\n\t"));

if (var_ano % 4 == 0 and var_ano % 100 != 0) or (var_ano % 400 == 0):
    print("O ano", var_ano, "é bissexto.\n\t");
else:
    print("O ano", var_ano, "não é bissexto.\n\t");
