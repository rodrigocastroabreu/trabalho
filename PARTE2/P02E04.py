#4) Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino,
#M - Masculino, Sexo Inválido.

var_caractere = input("Digite uma letra (F(Feminino) ou M(Masculino)):\n");

if var_caractere == 'F' or var_caractere == 'f':
    print("F - Feminino");
elif var_caractere == 'M' or var_caractere == 'm':
    print("M - Masculino");
else:
    print("Sexo Inválido");
