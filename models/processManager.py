# -*- coding: utf-8 -*-

# Bibliotecas
import psutil
from dynaconf import settings
import subprocess
import os
from pathlib import Path

class ProcessManager:
    def __init__ (self, process_name, file_name):
        self.process_name = process_name
        self.file_name = file_name

    def run(self):
        processes = [(i, psutil.Process(i).name()) for i in psutil.pids()] # lista todos os processo
        process = [(i, j) for i, j in processes if (j == self.process_name)] # Analise se existe um deteminado serviço em execução
        
        if ( len(process) < 1): # Caso não exista nenhum processo rodando.
            caminho = os.getcwd() # Obtem o caminho local  
            script = '{}{}{}'.format(caminho, settings.CONFIG.FilePath, self.file_name)
            if(Path(script).is_file()):
                subprocess.call("python {}".format(script), shell=True ) # Executa o script correspontente
            else:
                print ('Arquivo não encontrado.')
        else:
            print("O serviço está ok.")
