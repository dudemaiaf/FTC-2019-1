import re

def veririfcar_matricula (string):
    match = re.search(r'^([0-9]){10}$', string)
    if(match != None):
        return True
    else:
        return False

print(veririfcar_matricula("1615310003"))