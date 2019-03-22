import re

def verificar_nota (string):
    match = re.search(r'^(\d)([.])([0-9]{2})$',string)
    if(match != None):
        return True
    else:
        return False

print(verificar_nota("9.00"))