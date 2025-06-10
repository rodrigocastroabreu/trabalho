#24) Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma
#função de arredondamento.

var_numero = float(input("Qual o número?\n\t"));

if var_numero == round(var_numero):
    print("O número é inteiro\n\t", var_numero);
else:
    print("O número é decimal\n\t", var_numero);
