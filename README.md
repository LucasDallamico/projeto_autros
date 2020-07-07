# projeto_autros
Projeto de automação residência usando raspberry
*** ESTÁ EM FASE DE TESTE ***

## Objetivo
Usando o Django e REST_Framework, o objetivo é controlar vários pontos da casa usando um site da internet.
Os módulos serão controlados através das portas GPIO da raspberry

## Requisitos minimos
Python 3.6
SSH

## Instalação
Basta executar o script "install_requeres.sh"

## Execução

### Servidor
basta executar o arquivo "start_servers.sh", ele abrirá duas janelas, uma para o servidor DJANGO e outra para a conexão com o SERVEO para acesso externo

### Interator raspberry
Executar o script em rasp/, usando o comando "python3 main_for_raspberry.py"


## Referencias para pacotes usados

### APACHE2 + Django tutorial
https://github.com/codingforentrepreneurs/Guides/blob/master/all/DjangoPiNetworkServerGuide.md

