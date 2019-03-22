import re

def verificar_creditos (string):
    match = re.search(r'^(\d)([,])([0-9]{2})$',string)
    if(match != None):
        return True
    else:
        return False

print(verificar_creditos("9,00"))