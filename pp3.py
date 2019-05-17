import ast
def verificar_entrada (mt, entrada):

    aux = []

    for x in range (len(entrada)):
        aux.append(entrada[x])
    aux.append('b')

    estado_atual = mt['inicial']
    cabecote = 0
    cond = False
    i = 0
    #print("Entrou 1")
    while not cond:
        while( aux[i] != 'b'):
            for j in range (len(mt['delta'])):
                #verificacao fita com transicao
                if(aux[cabecote] == mt['delta'][j][2]):
                    #verificar se esta no estado certo
                    if(estado_atual == mt['delta'][j][0]):
                        #troca de valores na fita
                        #print("Verificou a troca de valores")
                        aux[cabecote] = mt['delta'][j][3]

                        #movimento cabecote
                        if(mt['delta'][j][4] == 'D'):
                            cabecote = cabecote + 1
                            i = i + 1
                        elif(mt['delta'][j][4] == 'E'):
                            cabecote = cabecote - 1
                            i = i + 1
                        elif(mt['delta'][j][4] == 'P'):
                            pass

                        #atualizar o estado atual
                        estado_atual = mt['delta'][j][1]

                    else:
                        pass

                else:
                    pass
        cond = True
        if(estado_atual == mt['aceita']):
            string = " ACEITA"
        else:
            string = " REJEITA"
            
    
    saida = ''
    for y in range (len(aux)):
        if(aux[y] == '' or aux[y] == 'b'):
            pass
        else:
            saida += aux[y]
    saida += string
    #print("Vai sair")
    return saida 





#mt = {'inicial': 0,'aceita': 1,'delta': [(0,0,'0','1','D'), (0,0,'1','0','D'), (0,2,'b','b','E'), (2,1,'0','0','P'), (2,1,'1','1','P')]}
#entrada = '000000000'

#print(criar_lista(mt, entrada))


def ler_linhas ():
    mt = ast.literal_eval(input())
    return mt

mt = ler_linhas()
n = int(input())
string = ''
for i in range (0,n):
    #print(string, i)
    entrada = str(input())
    string += verificar_entrada(mt, entrada)
    if(i != (n - 1)):
        string += '\n'
    

print(string)