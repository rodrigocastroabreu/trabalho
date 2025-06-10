#9) Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.

var_valor1 = float(input("Qual valor do primeiro produto?\n\t"));
var_valor2 = float(input("Qual valor do segundo produto?\n\t"));
var_valor3 = float(input("Qual valor do terceiro produto?\n\t"));

if var_valor1 < var_valor2 and var_valor1 < var_valor3:
    print("O primeiro produto é mais barato", var_valor1);
elif var_valor2 < var_valor1 and var_valor2 < var_valor3:
    print("O segundo produto é mais barato\n\t",var_valor2);
else:
    print("O terceiro produto é mais barato\n\t",var_valor3);
