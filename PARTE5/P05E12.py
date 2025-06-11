#12) Foram anotadas as idades e alturas de 30 alunos.
#Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

var_idades = [];
var_alturas = [];
var_i = 1;
while var_i <= 30:
    print("Aluno", var_i, ":");
    idade = int(input("Qual idade?\n\t"));
    altura = float(input("Qual altura?\n\t"));
    var_idades.append(idade);
    var_alturas.append(altura);
    var_i += 1;

var_soma_alturas = 0;
var_i = 0;
while var_i < 30:
    var_soma_alturas += var_alturas[var_i];
    var_i += 1;

var_media = (var_soma_alturas / 30);

var_contador = 0;
var_i = 0;
while var_i < 30:
    if var_idades[var_i] > 13 and var_alturas[var_i] < var_media:
        var_contador += 1;
    var_i += 1;

print("Número de alunos é:\n\t", var_contador);
