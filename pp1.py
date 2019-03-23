import re


"""VERIFICADOR DO NOME NO CABECALHO"""
def verificar_nome(string):
    match = re.search(r'^((N)(o)(m)(e)(:)( ))([A-Z|a-z| ]{1,50})$',string)
    if(match != None):
        aux = []
        for i in range (len(string)):
            aux.append(string[i])
        if(aux[6] == " "):
            return False
        else:
            return True
    else:
        return False

"""VERIFICADOR DO CPF NO CABECALHO"""
def verificar_cpf(string):
    parte1 = ""
    parte2 = ""
    flag = False
    for i in range (len(string)):
        if(string[i] == " "):
            if(flag == False):
                parte1 += string[i]
                flag = True
        else:
            if(flag == True):
                parte2 += string[i]
            else:
                parte1 += string[i]
    match = re.search(r'^((C)(P)(F)(:)( ))$',parte1)
    if(match != None):
        match2 = re.search(r'^([0-9]{3}).([0-9]{3}).([0-9]{3})-([0-9]{2})$',parte2)
        if(match2 != None):
            confirmacao1 = False
            confirmacao2 = False
            aux = []
            """VERIFICACAO DO PRIMEIRO DIGITO"""
            for i in range (len(parte2)):
                if(parte2[i] == "." or parte2[i] == "-"):
                    flag = False
                else:
                    aux.append(parte2[i])

            a = 10
            acumulador1 = 0
            for x in range (len(aux)-2):
                acumulador1 = acumulador1 + (int(aux[x]) * a)
                a = a - 1
            verificador1 = ((acumulador1 * 10) % 11)
            if(verificador1 == 10):
                verificador1 = 0
                if(verificador1 == aux[9]):
                    confirmacao1 = True
                else:
                    confirmacao1 = False
            else:
                if(verificador1 == int(aux[9])):
                    confirmacao1 = True
                else:
                    confirmacao1 = False
            """VERIFICACAO DO SEGUNDO DIGITO"""
            if(confirmacao1):
                b = 11
                acumulador2 = 0
                for m in range(len(aux) - 1):
                    acumulador2 = acumulador2 + (int(aux[m]) * b)
                    b = b - 1
                verificador2 = ((acumulador2 * 10) % 11)
                if(verificador2 == int(aux[10])):
                    confirmacao2 = True
                else:
                    confirmacao2 = False
            else:
                return False

            if(confirmacao1 == True and confirmacao2 == True):
                return True
            else:
                return False
        else:
            return None
    else:
        return False


"""VERIFICAR A MATRICULA DO ALUNO"""
def veririficar_matricula (string):
    match = re.search(r'^((M)(a)(t)(r)(i)(c)(u)(l)(a)(:)( ))([0-9]{10})$', string)
    if(match != None):
        return True
    else:
        return False


"""VERIFICADOR DO SEPARADOR DO CABECALHO"""
def verificar_separador (string):
    match = re.search(r'^([-]{20})$',string)
    if(match != None):
        return True
    else:
        return False


def verificar_linha (string):
    match = re.search(r'^(([0-9]{4})([/]{1})([1-2]{1})([-]{1})([1-2]{1})) (([E])([S])([T])(((B)(S)(I))|((E)(C)(P))|((B)(A)(S))|((L)(I)(C)))([0-9]{3})) ((["]{1})([A-Za-z, ]+)([0-9]?)(["]){1}) ((((B)(S)(I))|((E)(C)(P))|((E)(N)(G))|((L)(I)(C)))(([0-9]{2})|((T)(P)(F)))([_])([T])([0-9]{2})) ((\d)([,])([0-9]{2})) ((\d){1,2}([.])([0-9]{2})) ((((A)(P)(R)(O)(V)(A)(D)(O))|((R)(E)(P)(R)(O)(V)(A)(D)(O))))$',string)
    if(match != None):
        return True
    else:
        return False

"""VERIFICAR O CABECALHO"""

def verificar_cabecalho (string):
    nome = ""
    cpf = ""
    matricula = ""
    separador = ""
    linha = ""
    contador_quebra = 0
    linhas_erradas = []
    acumulador_nota_credito = 0
    acumulador_credito = 0
    verificador_de_status = False
    CRE = 0
    for i in range (len(string)):
        if(string[i] == "\n"):
            contador_quebra += 1
            if(contador_quebra > 4):
                linha +=string[i]

        else:
            if(contador_quebra == 0):
                nome += string[i]

            if(contador_quebra == 1):
                cpf += string[i]

            if(contador_quebra == 2):
                matricula += string[i]

            if(contador_quebra == 3):
                separador += string[i]

            if(contador_quebra > 3):
                linha += string[i]

    quebrar_linha = linha.split("\n")
    for j in range (len(quebrar_linha)):
        v = verificar_linha(quebrar_linha[j])
        if(v == False):
            linhas_erradas.append(j)
        else:
            x = quebrar_linha[j].split()
            x[-3] = x[-3].replace(",",".")
            vector = []
            vector.append(x[-3])
            vector.append(x[-2])

            for z in range (len(vector)):
                vector[z] = float(vector[z])


            if(x[-1] == "APROVADO" and vector[1] >= 6.00):
                verificador_de_status = True
                acumulador_nota_credito = acumulador_nota_credito + (vector[0] * vector[1])
                acumulador_credito = acumulador_credito + (vector[0])

    if(acumulador_credito == 0 or acumulador_nota_credito == 0):
        CRE = 0
    else:
        CRE = acumulador_nota_credito / acumulador_credito
    CRE = round(CRE,2)
    if(verificar_nome(nome) == True):
        if(verificar_cpf(cpf) == True):
            if(veririficar_matricula(matricula) == True):
                if(verificar_separador(separador) == True):
                    if(linhas_erradas == []):
                        saida = (
                            "CABECALHO VALIDO"
                            "\n"
                            f"CRE: {CRE}"
                        )
                        return saida
                    else:
                        saida = (
                            "CABECALHO VALIDO"
                            "\n"
                            "LINHAS INVALIDAS:"
                            "\n"
                        )
                        for m in range (len(linhas_erradas)):
                            saida += "LINHA 0"
                            saida += str(linhas_erradas[m])
                            saida += "\n"
                        saida += f"CRE: {CRE}"

                        return saida
                else:
                    return "CABECALHO INVALIDO"
            else:
                return "CABECALHO INVALIDO"
        else:
            return "CABECALHO INVALIDO"
    else:
        return "CABECALHO INVALIDO"


#MAIN
entrada_nome = input()
entrada_handle = open(entrada_nome,"r")
tudo = entrada_handle.read()
print(verificar_cabecalho(tudo))
entrada_handle.close()