#15) A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de
#gerar a série até o n−ésimo termo.

var_n = int(input("Qual o valor de n?\n\t"));

var_termo1 = 1;
var_termo2 = 1;

var_i = 1;
while var_i <= var_n:
    print("\n\t", var_termo1);

    var_proximo = var_termo1 + var_termo2;
    var_termo1 = var_termo2;
    var_termo2 = var_proximo;

    var_i += 1;

