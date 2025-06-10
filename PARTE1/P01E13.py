#13) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
#diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
#regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
#excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule
#o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor
#da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas

var_limite_estabelecido = 50;
var_valor_multa = 4;

var_peso = float(input("Digite peso dos peixes:\n"));

if var_peso > var_limite_estabelecido:
    var_excesso = var_peso - var_limite_estabelecido;
    var_multa = var_excesso * var_valor_multa;
else:
    var_excesso = 0;
    var_multa = 0;

print("O peso é:",var_peso);
print("O excesso é:",var_excesso);
print("O multa é:",var_multa);
