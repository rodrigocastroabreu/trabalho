#10) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo .
#b) a soma do triplo do primeiro com o terceiro.
#c) o terceiro elevado ao cubo.

var_int_numero1 = int(input("Digite um numero inteiro:\n"));
var_int_numero2 = int(input("Digite um numero inteiro novamente\n"));
var_float_numero3 = float(input("Digite um número real float:\n"));

#a)
var_letra_a = ((var_int_numero1*2) * (var_int_numero2/2));
print("a) O produto do dobro do primeiro com metade do segundo é:\n",var_letra_a);

#b
var_letra_b = ((var_int_numero1*3) + var_float_numero3);
print("b) a soma do triplo do primeiro com o terceiro é:\n",var_letra_b);

#c
var_letra_c = (var_float_numero3 **3);
print("c) o terceiro elevado ao cubo é:\n",var_letra_c);





