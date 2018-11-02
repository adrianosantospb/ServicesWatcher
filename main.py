# -*- coding: utf-8 -*-

'''
Projeto GASIS F3
Script de exemplo para verificação da existencia de processos
Por Adriano Santos

https://www.youtube.com/watch?v=VOzvpHoYQoo

'''

# Bibliotecas
import getopt
import sys
from dynaconf import settings
from models.machineManager import MachineManager


# Variáveis
machine_name = ''

if __name__ == '__main__':
        # Obtem os valores dos parâmetros e argumentos
    try:
        optlist, _ = getopt.getopt(sys.argv[1:], 'm:i')
        machine_name = [arg for opt, arg in optlist if (opt == settings.CONFIG.Parameter)]
    except getopt.GetoptError as e:
        print('Erro no processamento. Verifique se o parametro -m foi informado. ', e)
    
    try:
        if (len(machine_name) > 0):
            machineManager = MachineManager(machine_name[0])
            machineManager.run()
        else:
            print('Nenhum processo foi informado.')

    except Exception as identifier:
        print(identifier)
    