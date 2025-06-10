#21) Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média
#alcançada por aluno e presentar:
#A) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#B) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#C) A mensagem "Aprovado com Distinção", se a média for igual a 10.

var_primeira_nota1 = float(input("Qual a primeira nota:\n\t"));
var_segunda_nota2 = float(input("Qual a segunda nota:\n\t"));
var_terceira_nota3 = float(input("Qual a terceira nota:\n\t"));

var_calcular_media = ((var_primeira_nota1 + var_segunda_nota2 + var_terceira_nota3) / 3);

if var_calcular_media >= 7:
    print("Aprovado\n\t", var_calcular_media);
elif var_calcular_media < 7:
    print("Reprovado\n\t", var_calcular_media);
elif var_calcular_media == 10:
    print("Aprovado com Distinção\n\t", var_calcular_media);
