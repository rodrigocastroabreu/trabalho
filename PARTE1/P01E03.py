# 3. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

Var_Nota1 = float(input("Digite Nota1: "));
Var_Nota2 = float(input("Digite Nota2: "));
Var_Nota3 = float(input("Digite Nota3: "));
Var_Nota4 = float(input("Digite Nota4: "));

Var_Aux = ((Var_Nota1+Var_Nota2)/2);
Var_Aux2 = ((Var_Nota3+Var_Nota4)/2);

Var_Media = ((Var_Aux+Var_Aux2)/2);

print("A média é: ", Var_Media);