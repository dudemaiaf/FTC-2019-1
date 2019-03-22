import re

def verificar_semestre (string):
    match = re.search(r'^([0-9]{4})+([/]{1})+([1-2]{1})+([-]{1})+([1-2]{1})$',string)
    if(match != None):
        return True
    else:
        return False

print(verificar_semestre("2014/1-1"))