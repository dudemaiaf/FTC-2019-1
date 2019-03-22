import re

def verificar_cpf(string):
    match = re.search(r'^([0-9]{3}).([0-9]{3}).([0-9]{3})-([0-9]{2})$',string)
    if(match != None):
        """Verificação do Primeiro Digito"""
        vetor = []
        tamanho = len(string) - 3
        contador = 0
        verificacao1 = 0
        multiplicador = 2
        for i in range(contador,tamanho):
            vetor.append(string[i])
        vetor.reverse()
        for j in range(contador,tamanho):
            if(string[j] != '.' and string[j] != '-'):
                verificacao1 = verificacao1 + (int(vetor[j])*multiplicador)
                multiplicador = multiplicador + 1
            else:
                multiplicador = multiplicador
        verificacao1 = verificacao1 % 11
        if(verificacao1 < 2):
            if(int(string[12]) == 0):
                return True
            else:
                return False
        else:
            verificacao1 = 11 - verificacao1
            """verificacao do segundo digito"""
            if(int(string[12]) == verificacao1):
                vetor.reverse()
                vetor.append('-')
                vetor.append(verificacao1)
                vetor.reverse()
                verificacao2 = 0
                contador = 0
                tamanho = len(string)-1
                multiplicador = 2
                for h in range(contador,tamanho):
                    if(vetor[h] != '.' and vetor[h] != '-'):
                        verificacao2 = verificacao2 + (int(vetor[h])*multiplicador)
                        multiplicador = multiplicador + 1
                    else:
                        multiplicador = multiplicador
                verificacao2 = verificacao2 % 11                
                if(verificacao2 < 2):
                    if(int(string[13]) == 0):
                        return True
                    else:
                        return False
                else:
                    verificacao2 = 11 - verificacao2
                    if(int(string[13]) == verificacao2):
                        return True
                    else:
                        return False
            else:
                return False
    else:
        return False


cpf = str(input("Digite seu cpf: "))
print(verificar_cpf(cpf))