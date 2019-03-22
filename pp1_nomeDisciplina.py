import re

def verificar_nomeDisciplina (string):
    match = re.search(r'^([A-Za-z, \b]+)([0-9]?)$',string)
    if(match != None):
        return True
    else:
        return False
    

print(verificar_nomeDisciplina("Algoritmo e Estrutura de Dados 2"))