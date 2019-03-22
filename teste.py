import re

def verificar_APP (string):
    APP = re.search(r'^(s?).*$',string)
    if (APP != None):
        return True
    else:
        return False

string = "2017/1-1 ESTBAS002 \n'Sistemas de informa'\n ENG01_T01 6,00 7.00 APROVADO"

a = re.search(r'^([0-9]{4})+([/]{1})+([1-2]{1})+([-]{1})+([1-2]{1}) ([E])([S])([T])(((B)(S)(I))|((E)(C)(P))|((B)(A)(S))|((L)(I)(C)))([0-9]{3}) \"([A-Za-z, \b]+)([0-9]?)\" (((B)(S)(I))|((E)(C)(P))|((E)(N)(G))|((L)(I)(C)))(([0-9]{2})|((T)(P)(F)))([_])([T])([0-9]{2}) (\d)([,])([0-9]{2}) (\d)([.])([0-9]{2}) (((A)(P)(R)(O)(V)(A)(D)(O))|((R)(E)(P)(R)(O)(V)(A)(D)(O)))$', string)

b = string.split("\n")

c = """texte
teste
texto"""
print(c)


#print(b)
#print(b[-3], b[-2], a)
#print(verificar_APP("Waze"))