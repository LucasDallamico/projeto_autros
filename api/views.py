from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json

def faz_alteracao_dados_brutos(str_site, dic_de_dados):
    if str_site == "Lampada 1":
        if dic_de_dados['lamp1'] == 0:
            dic_de_dados['lamp1'] = 1
        else:
            dic_de_dados['lamp1'] = 0

    elif str_site == "Lampada 2":
        if dic_de_dados['lamp2'] == 0:
            dic_de_dados['lamp2'] = 1
        else:
            dic_de_dados['lamp2'] = 0

    return dic_de_dados


def inicio(request):

    if request.method =='POST':
        # Obter a alteração da vez
        qual_alterou = request.POST['lamp']

        # Obtem os registros da gambiarra
        with open("gambiarra.json", "r") as arq:
            dados_brutos = json.load(arq)

        dados_atualizados = faz_alteracao_dados_brutos(qual_alterou, dados_brutos)

        # salva as alteracoes no arquivo
        with open("gambiarra.json", "w") as arq:
            json.dump(dados_atualizados, arq, indent=4, sort_keys=False)

    return render(request, 'inicio.html')
    

def descricao(request):
    return render(request, 'descricao.html')

def contato(request):
    return render(request, 'contato.html')

def redirect_contato(request):
    response = redirect('/contato/')
    return response

@api_view(['GET'])
def estado_rasp(request):
    if request.method == 'GET':
        # Obtem os registros da gambiarra
        with open("gambiarra.json", "r") as arq:
            dados_dos_modulos = json.load(arq)

        return Response(dados_dos_modulos, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'operacao nao permitida'})
