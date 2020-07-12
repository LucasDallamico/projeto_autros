# -------------------------------------
import json
import requests
import pickle
import time
# Raspberry
import RPi.GPIO as GPIO
# Lembrar de escolhers a portas com sabedoria
# -------------------------------------
# Urls de interação

url_request = (
    "https://projeto-autros.herokuapp.com/estado_rasp/"
)

# Portas GPIO USADAS
porta_lamp1 = 16
porta_lamp2 = 18

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
        GPIO.output(porta_lamp1,(not self.lamp1))
        GPIO.output(porta_lamp2,(not self.lamp2))
        #print(self.lamp1,self.lamp2)

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
    GPIO.setmode(GPIO.BOARD)
    # Setando as portas como saida
    GPIO.setup(porta_lamp1, GPIO.OUT)
    GPIO.setup(porta_lamp2, GPIO.OUT) 
    #GPIO.setup(16, GPIO.IN)
    """
    GPIO.output(18,0)
    GPIO.output(16,0)
    time.sleep(10) #Esperar 5 segundos
    GPIO.output(18,0)
    GPIO.output(16,0)
    GPIO.cleanup()
    """
    my_modulos = modulos()
    while(True):
        try:
            estados_em_dic = solicita_estado_modulos()
            #print(estados_em_dic)
            my_modulos.set_estados_modulos(estados_em_dic)
        except:
            pass
            #print("Não foi possível solicitar a página")
        time.sleep(5) #Esperar 5 segundos
    #limpa a reserva das portas
    GPIO.cleanup()