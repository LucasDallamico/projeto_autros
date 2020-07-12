# projeto_autros
Projeto de automação residência usando raspberry

*** Esta em contrução *** 

mas já está funcional

## Objetivo
Usando o Django e REST_Framework, o objetivo é controlar vários pontos da casa usando um site da internet.
Os módulos serão controlados através das portas GPIO da raspberry

## Requisitos minimos
Python 3.6
Heroku - Serviço que vai hospedar o site
Guinicorn

## Instalação
Os passos para você upar o servidor no heroku estão no arquivo passo_passo_deplouy.txt

## Execução

### Servidor
basta executar o arquivo "start_servers.sh", ele abrirá duas janelas, uma para o servidor DJANGO e outra para a conexão com o SERVEO para acesso externo

### Interator raspberry
Os arquivos para instalar na raspberry estãona pasta controle_RASP, lembre-se de instalar os pacote do python que irá usar

pip install -r requeriments.txt

Na pasta controle_RASP, tem os arquivos e passos para configurar

## Referencias para pacotes usados


