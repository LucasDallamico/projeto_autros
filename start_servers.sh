# -*- coding: utf-8 -*-
#!/bin/bash
echo ligando os servers ...
gnome-terminal -- 'cd web/PROJETO_AUTROS/; python3 manage.py runserver'
gnome-terminal -- 'ssh -R 80:localhost8000 serveo.net'