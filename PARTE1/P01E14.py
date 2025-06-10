#14) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
#Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a) salário bruto.
#b) quanto pagou ao INSS.
#c) quanto pagou ao sindicato.
#d) o salário líquido.
#e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

var_ganha_hora = float(input("Quanto você ganha por hora? "));
var_horas_trabalhadas = float(input("Número de horas trabalhadas por mês? "));

var_salario_bruto = var_ganha_hora * var_horas_trabalhadas;

var_ir = var_salario_bruto * 0.11;
var_inss = var_salario_bruto * 0.08;
var_sindicato = var_salario_bruto * 0.05;

var_descontos = var_ir + var_inss + var_sindicato;
var_salario_liquido = var_salario_bruto - var_descontos;

print("salário bruto", var_salario_bruto);
print("IR", var_ir);
print("INSS",var_inss);
print("sindicato", var_sindicato);
print("salário líquido",var_salario_liquido);
