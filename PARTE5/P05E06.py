#6) Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

var_aprovados = 0;
var_aluno = 1;
while var_aluno <= 10:
    var_soma = 0;
    var_nota = 1;

    print("Aluno", var_aluno);

    while var_nota <= 4:
        var_soma += float(input("Nota?\n\t"));
        var_nota += 1;

    var_media = var_soma / 4;

    if var_media >= 7:
        var_aprovados += 1;

    var_aluno += 1;

print("Qtd alunos com média >= 7:\n\t", var_aprovados);
