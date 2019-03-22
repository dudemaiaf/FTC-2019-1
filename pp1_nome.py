import re 

def verificar_nome(string):
    match = re.search(r'^((N)(o)(m)(e)(:)( ))([A-Z|a-z| ]{1,50})$',string)
    if(match != None):
        aux = []
        for i in range (len(string)):
            aux.append(string[i])
        print(aux)
        if(aux[6] == " "):
            return False
        else:
            return True
    else:
        return False


print(verificar_nome("Nome: Eduardo"))