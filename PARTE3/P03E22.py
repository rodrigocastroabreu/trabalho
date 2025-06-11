#22) Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais
#número ele é divisível.

var_numero = int(input("Qual o número?\n\t"));

var_divisor = 0;
var_i = 1;
var_divisores = [];
while var_i <= var_numero:
    if var_numero % var_i == 0:
        var_divisor += 1;
        var_divisores.append(var_i);
    var_i += 1;

if var_divisor == 2:
    print("É número primo\n\t");
else:
    print("Não é número primo\n\t");
    print("Ele é divisível por:\n\t", var_divisores);
