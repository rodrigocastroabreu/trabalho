#34) Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um
#número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um
#número inteiro e determine se ele é ou não um número primo.

var_numero = int(input("Qual número?\n\t"));

var_divisor = 0;
var_i = 1;
while var_i <= var_numero:
    if var_numero % var_i == 0:
        var_divisor += 1;
    var_i += 1;

if var_divisor == 2:
    print("É número primo\n\t");
else:
    print("Não é número primo\n\t");
