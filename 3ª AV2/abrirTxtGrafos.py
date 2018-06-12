''' Este arquivo é apenas um teste para saber como implementar da melhor forma de leitura e escrita de dados no arquivo.txt'''

import re,os
'''Funções Úteis:
pasta = diretorio\\do\\arquivo
arq = open(pasta+'nomedoarquivo.extensao')
le = arq.read() #lê completo| le = arq.readlines() #Separa por linhas EX:le[0]
le.split(',') #padrão para separação dos dados.
arq.write('\nTá, mano') #Escreve algo no arquivo.
'''

#Funções auxiliares
def is_float(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def is_int(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


#pasta = 'C:\\Users\\Jairo\\Desktop\\';
pasta = os.path.dirname(os.path.realpath(__file__))
arq = open(pasta+'\\Grafos\\grafo_H.txt','r+')
le = arq.readlines();
#le = arq.read();
arq.close()

#Salvar Vertice
arq2 = open(pasta+'\\Grafos\\teste.txt','w')
tes = le[0].split(',')
tes[-1] = tes[-1].replace("\n","") 
arq2.write("[")
for i in range(len(tes)-1):
    arq2.write("{}, ".format(tes[i]))
arq2.write("{}]".format(tes[-1]))
arq2.write("\n")
arq2.close()

#Salvar Aresta
arq3 = open(pasta+'\\Grafos\\teste.txt','a')
tes = le[1].split(',')
tes[-1] = tes[-1].replace("\n","") 
arq3.write("[")
for i in range(0,len(tes)-2,2):
    arq3.write("{},{}, ".format(tes[i],tes[i+1]))
arq3.write("{},{}]".format(tes[-2],tes[-1]))
arq3.write("\n")
arq3.close()

#Salvar Valor da aresta
arq4 = open(pasta+'\\Grafos\\teste.txt','a')
tes = le[2].split(',')
tes[-1] = tes[-1].replace("\n","") 
arq4.write("[")
for i in range(len(tes)-1):
    if is_int(tes[i]):
        arq4.write("{}, ".format(int(tes[i])))
    elif is_float(tes[i]):
        arq4.write("{}, ".format(float(tes[i])))
    else:
        arq4.write("{}, ".format(tes[i]))
arq4.write("{}]".format(tes[-1]))
arq4.write("\n")
arq4.close()

