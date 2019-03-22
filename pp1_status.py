import re

def verificar_status (string):
    match = re.search(r'^(((A)(P)(R)(O)(V)(A)(D)(O))|((R)(E)(P)(R)(O)(V)(A)(D)(O)))$', string)
    if(match != None):
        return True
    else:
        return False

print(verificar_status("APROVADO"))