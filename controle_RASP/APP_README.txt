ANOTAÇÔES
--------------------------------------------------------
Para instalar no boot o arquivo, basta executar o script

$bash script_control_autros.sh

--------------------------------------------------------
Para colocar um script para inicializar no boot da rasp

nano nome_do_script

[Unit]
Description=Projeto Autros inicializado ...
[Service]
Type=simple
ExecStart=/home/lucas/projeto_autros/rasp/"python3 main.py"
#ExecStop="Escript para desligar, n�o vou usar, serve para desligar corretamente"
[Install]
WantedBy=multi-user.target

--> Copiar para o diretorio:
sudo cp "nomedoscripy" /lib/systemd/system/ 

--> Preciso dizer para o sytemdD que tem um novo processo
sudo systemctl enable "nome_do_script"

para verificar se o servi�o est� ativo
sudo systemctl status "nome_do_script"

obs: Vou usar um scritp de desligar a rasp para liberar as portas da GPIO, talves

Posso controlar o processo
sudo systemctl stop "processo"
sudo systemctl start "processo"

