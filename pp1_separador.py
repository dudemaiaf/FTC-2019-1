import re

def verificar_separador (string):
    match = re.search(r'^([-]{20})$',string)
    if(match != None):
        return True
    else:
        return False

print(verificar_separador("--------------------"))