import re 

def verificar_nomeTurma (string):
    match = re.search(r'^([E])([S])([T])(((B)(S)(I))|((E)(C)(P))|((E)(N)(G))|((L)(I)(C)))(([0-9]{2})|((T)(P)(F)))([_])([T])([0-9]{2})$',string)
    if(match != None):
        return True
    else:
        return False

"""print(verificar_nomeTurma("ECP01_T09"))"""

print(verificar_nomeTurma("ESTBSI00_T09"))