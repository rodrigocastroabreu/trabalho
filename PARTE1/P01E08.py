#Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em
#graus Celsius. C = 5 * ((F-32) / 9).

var_temperatura_Fahrenheit = float(input("Qual temperatura em Fahrenheit?\n"));

var_temperatura_Celsius = 5 * ((var_temperatura_Fahrenheit -32)/9);

print("A temperatura em graus Celsius é:\n",var_temperatura_Celsius);
