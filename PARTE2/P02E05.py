#5) Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

var_caractere = input("Digite uma letra:\n").lower();

var_vogal = ('a', 'e', 'i', 'o', 'u');
var_consoante = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z');

if var_caractere in var_vogal:
    print("É uma vogal.");
elif var_caractere in var_consoante:
    print("É uma consoante.");
else:
    print("Não é uma letra.");
