# -------------------------------------
import json
import requests
import pickle
import time
# Raspberry
#import RPi.GPIO as GPIO
# Lembrar de escolhers a portas com sabedoria
# -------------------------------------
# Urls de interação
url_request = (
    "http://127.0.0.1:8000/estado_rasp/"
)

# -------------------------------------
def solicita_estado_modulos() -> dict:
    '''
    Função obtem o json do servidor

    '''
    resposta_server_json = requests.get(url_request)
    if resposta_server_json:
        # salva em modo dicionário
        dic_dados = json.loads(resposta_server_json.content)
        return dic_dados
    else:
        return None

# -------------------------------------
class modulos():
    # Bools de estado
    lamp1 = 0
    lamp2 = 0

    def set_estados_modulos(self, dados_em_dic):
        self.lamp1 = dados_em_dic["lamp1"]
        self.lamp2 = dados_em_dic["lamp2"]
        # PORTA e ESTADO [ 0 des, 1 lig ]
        #GPIO.output(12,self.lamp1)
        #GPIO.output(16,self.lamp2)
        print(self.lamp1,self.lamp2)

# -------------------------------------
if __name__ == "__main__":
    """
    Aqui definimos que vamos usar o numero de 
    ordem do pino, e não o numero que refere 
    a porta.
    Para usar o numero da porta, é preciso trocar
    a definição "GPIO.BOARD (ex. Pino 12)" para 
    "GPIO.BCM (ex.GPIO 18)"
    """
    #GPIO.setmode(GPIO.BOARD)
    # Setando as portas como saida
    #GPIO.setup(12, GPIO.OUT) # lamp1
    #GPIO.setup(16, GPIO.OUT) #lamp 2
    #GPIO.setup(16, GPIO.IN)
    my_modulos = modulos()
    while(True):
        try:
            estados_em_dic = solicita_estado_modulos()
            print(estados_em_dic)
            my_modulos.set_estados_modulos(estados_em_dic)
        except:
            print("Não foi possível solicitar a página")
        time.sleep(5) #Esperar 5 segundos