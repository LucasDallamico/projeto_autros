echo "Instalando os arquivos no boot da raspberry ..."
sudo cp "script_controle_rasp" /lib/systemd/system/
sudo systemctl enable "script_controle_rasp"
echo "Processo realizado com sucesso!"
