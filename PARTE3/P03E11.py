#11) Altere o programa anterior para mostrar no final a soma dos números.

var_numero1 = int(input("Qual primeiro número?\n\t"));
var_numero2 = int(input("Qual segundo número?\n\t"));

var_menor = min(var_numero1, var_numero2);
var_maior = max(var_numero1, var_numero2);

print("O intervalo compreendido por eles é:\n\t");

var_i = var_menor + 1;
var_soma = 0;
while var_i < var_maior:
    print("\n\t", var_i);
    var_soma += var_i;
    var_i += 1;

print("A soma dos números é:\n\t", var_soma);
