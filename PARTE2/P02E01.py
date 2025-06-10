#1) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link
#de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

var_tamanho_arquivo_mb = float(input("Qual o tamanho do arquivo para download (MB)?\n"));

var_velocidade_internet_mbps = float(input("Qual a velocidade do link de Internet (Mbps)?\n"));

var_velocidade_internet_mbps = (var_velocidade_internet_mbps / 8);
var_tempo_download_segundos = var_tamanho_arquivo_mb / var_velocidade_internet_mbps;
var_tempo_download_minutos = (var_tempo_download_segundos / 60);

print("O tempo aproximado de download do arquivo é:\t", var_tempo_download_minutos);
