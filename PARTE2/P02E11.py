#11) Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino
#ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

var_turno = input("Qual seu turno? m-matutino, v-vespertino, n-noturno\n\t").lower();

if var_turno == 'm':
    print("Bom Dia!\n\t");
elif var_turno == 'v':
    print("Boa Tarde!\n\t");
elif var_turno == 'n':
    print("Boa Noite!\n\t");
else:
    print("Valor Inválido!\n\t");
