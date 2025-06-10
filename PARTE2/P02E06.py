#6) Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

var_primeira_nota1 = float(input("Qual a primeira nota:\n\t"));
var_segunda_nota2 = float(input("Qual a segunda nota:\n\t"));

var_calcular_media = ((var_primeira_nota1 + var_segunda_nota2) / 2);

if var_calcular_media >= 7:
    print("Aprovado\n");
elif var_calcular_media < 7:
    print("Reprovado\n");
elif var_calcular_media == 10:
    print("Aprovado com Distinção\n");
