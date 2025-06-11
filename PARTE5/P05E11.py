#11) Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

var_vetor1 = [];
var_vetor2 = [];
var_vetor3 = [];
var_intercalado = [];
print("Vetor 1:");
var_i = 1;
while var_i <= 10:
    num = int(input("Qual valor?\n\t"));
    var_vetor1.append(num);
    var_i += 1;

print("Vetor 2:");
var_i = 1;
while var_i <= 10:
    num = int(input("Qual valor?\n\t"));
    var_vetor2.append(num);
    var_i += 1;

print("Vetor 3:");
var_i = 1;
while var_i <= 10:
    num = int(input("Qual valor?\n\t"));
    var_vetor3.append(num);
    var_i += 1;

var_i = 0;
while var_i < 10:
    var_intercalado.append(var_vetor1[var_i]);
    var_intercalado.append(var_vetor2[var_i]);
    var_intercalado.append(var_vetor3[var_i]);
    var_i += 1;

print("Vetor 1:", var_vetor1);
print("Vetor 2:", var_vetor2);
print("Vetor 3:", var_vetor3);
print("Vetor intercalado:", var_intercalado);
