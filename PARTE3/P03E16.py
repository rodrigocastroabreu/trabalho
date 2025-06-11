#16) A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a
#série até que o valor seja maior que 500.

var_termo1 = 1;
var_termo2 = 1;

var_i = 1;
while var_termo1 <= 500:
    print("\n\t", var_termo1);

    var_proximo = var_termo1 + var_termo2;
    var_termo1 = var_termo2;
    var_termo2 = var_proximo;

    var_i += 1;
