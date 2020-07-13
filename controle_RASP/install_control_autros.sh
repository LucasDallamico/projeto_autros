echo "Instalando os arquivos no boot da raspberry ..."
sudo apt-get install python3-rpi.gpio
sudo cp "controle_autros.service" /lib/systemd/system/
sudo systemctl start "controle_autros.service"
sudo systemctl status "controle_autros.service"
sudo systemctl enable "controle_autros.service"
echo "Processo realizado com sucesso!"
