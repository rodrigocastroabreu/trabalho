#12) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print("Algoritmo para calcular peso ideal.");
print("Para homens digite 1:");
print("Para mulheres digite 2:\n");

var_qual_genero_selecionado = input("Escolha (1 ou 2):\n");

var_altura = float(input("Qual sua altura?\n"));

if var_qual_genero_selecionado == "1":
    var_peso_ideal = (72.7 * var_altura) - 58;
    print("Peso para homens: (72.7*h) - 58 é:\n",var_peso_ideal);

if var_qual_genero_selecionado == "2":
    var_peso_ideal = (62.1 * var_altura) - 44.7;
    print("Peso para mulheres: (62.1*h) - 44.7 é:\n", var_peso_ideal);
