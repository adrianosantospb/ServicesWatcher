# -*- coding: utf-8 -*-

# Bibliotecas
from dynaconf import settings
from models.processManager import ProcessManager

class MachineManager:
    def __init__ (self, machine):
        machines_list = list (map(lambda x:x.lower(),settings.MACHINES.Names))
        if machine in machines_list:
            self.machine = machine.lower()
        else:
            raise Exception("Erro: Não existe nenhuma máquina chamada {}.".format(machine))
            
    def run(self): # Executa atividades de acordo com a máquina
        for i in range(len(settings.MACHINES.Names)): 
            if (settings.MACHINES.Names[i].lower() == self.machine):
                processManager = ProcessManager(settings.MACHINES.Processes[i].lower(),settings.MACHINES.Files[i].lower(), )
                processManager.run()