import re

def verificar_codigo (string):
    match = re.search(r'^([E])([S])([T])(((B)(S)(I))|((E)(C)(P))|((B)(A)(S))|((L)(I)(C)))([0-9]{3})$' ,string)
    if(match != None):
        return True
    else:
        return False

print(verificar_codigo("ESTBSI009"))