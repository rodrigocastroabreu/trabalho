#2) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
#usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    var_usuario = input("Qual nome de usuário?\n\t");
    var_senha = input("Qual sua senha?\n\t");

    if var_senha != var_usuario:
        print("Login feito com sucesso\n\t");
        break;
    else:
        print("Erro! A senha não pode ser igual ao nome de usuário.\n\t");
