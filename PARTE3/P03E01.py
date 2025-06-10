#1) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
#e continue pedindo até que o usuário informe um valor válido.

while True:
    var_nota = float(input("Digite uma nota entre 0 e 10:\n\t"));

    if 0 <= var_nota <= 10:
        print("A nota entre zero e dez é:\n\t", var_nota);
        break;
    else:
        print("Valor inválido! Tem que ser entre 0 e 10 \n\t");
