echo "Instalando os arquivos no boot da raspberry ..."
sudo cp "script_controle_rasp.service" /lib/systemd/system/
sudo systemctl enable "script_controle_rasp.service"
echo "Processo realizado com sucesso!"
