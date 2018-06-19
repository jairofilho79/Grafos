import os

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

''' Recebe, respectivamente, vértices, arestas e valores das arestas do arquivo.txt
    Esse arquivo é chamado pelo nome do grafo.'''
def recebe_vertices(nome):
  pasta = os.path.dirname(os.path.realpath(__file__))
  arq = open(pasta+'\\Grafos\\'+nome+'.txt','r+')
  le = arq.readlines();
  temp = le[0].split(',')
  temp[-1] = str(temp[-1]).replace("\n","")
  return temp

''' Aqui tem um problema de que as arestas são chamadas assim: '(1,2)'.
    Por isso, eu os quebro a cada vírgula, retiro os parênteses e a quebra de linha e depois remonto da forma correta.'''
def recebe_arestas(nome):
  pasta = os.path.dirname(os.path.realpath(__file__))
  arq = open(pasta+'\\Grafos\\'+nome+'.txt','r+')
  le = arq.readlines();
  temp = le[1].split(',')
  temp[-1] = str(temp[-1]).replace("\n","")
  for j in range(len(temp)):
    temp[j] = str(temp[j]).replace(" ","")
    temp[j] = str(temp[j]).replace("(","")
    temp[j] = str(temp[j]).replace(")","")
  temp2 = []
  for i in range(0,len(temp),2):
    temp2.append((int(temp[i]),int(temp[i+1])))
  return temp2

def recebe_arestas_transposta(nome):
  pasta = os.path.dirname(os.path.realpath(__file__))
  arq = open(pasta+'\\Grafos\\'+nome+'.txt','r+')
  le = arq.readlines();
  temp = le[1].split(',')
  temp[-1] = str(temp[-1]).replace("\n","")
  for j in range(len(temp)):
    temp[j] = str(temp[j]).replace(" ","")
    temp[j] = str(temp[j]).replace("(","")
    temp[j] = str(temp[j]).replace(")","")
  temp2 = []
  for i in range(0,len(temp),2):
    temp2.append((int(temp[i+1]),int(temp[i])))
  return temp2


''' Aqui eu faço questão de salvar valores que são float como float, int como int e string como string.
    Ainda não troquei o 'n' por 0. '''
def recebe_valor_arestas(nome):
  pasta = os.path.dirname(os.path.realpath(__file__))
  arq = open(pasta+'\\Grafos\\'+nome+'.txt','r+')
  le = arq.readlines();
  temp = le[2].split(',')
  temp[-1] = str(temp[-1]).replace("\n","")
  for j in range(len(temp)):
    if is_int(temp[j]):
      temp[j] = int(temp[j])
    elif is_float(temp[j]):
      temp[j] = float(temp[j])
  return temp

'''É uma lista onde conecta cada aresta com seu vértice de origem.
EX: profundidade['v'] = [(v,a),(v,b),(v,c)]. Serve para ganhar performance.
(Se não a cada iteração da profundidade, ele teria que fazer esse processo.'''
def cria_lista_profundidade(vertices,arestas):
    profundidade = {}
    for aresta in arestas:
        a,b = aresta
        if a in profundidade:
           profundidade[a].append(aresta)
        else:
            profundidade[a] = []
            profundidade[a].append(aresta)

    return profundidade

def rem_duplicado(lista):
    lista_final = []
    for l in lista:
        if l not in lista_final:
            lista_final.append(l)
    return lista_final

def busca_profundidade(lista_profundidade):
    cores = {}
    historico = []
    pilha = []
    vertices = sorted([*lista_profundidade])
    vertice = vertices[0]
    v_inicial = vertices[0]
    while True:
        while True:
            while True:
                indice_tupla = 0
                for x in range(len(lista_profundidade[vertice])):
                    #print(lista_profundidade[vertice][x])
                    a,b = lista_profundidade[vertice][x]
                    if b in cores:
                        c,d = lista_profundidade[vertice][indice_tupla]
                        if len(cores[b]) < len(cores[d]):
                            indice_tupla = x
                    else:
                      indice_tupla = x
                      break;
                #print('oie {}'.format(lista_profundidade[vertice][indice_tupla]))
                if vertice in cores:
                    #print(cores[vertice])
                    if len(cores[vertice]) == 2:
                        if vertice not in pilha:
                            pilha.append(vertice)
                        break;
                a,b = lista_profundidade[vertice][indice_tupla]
                historico.append(a)
                
                if vertice in cores:
                    cores[vertice].append(len(historico))
                else:
                    cores[vertice] = []
                    cores[vertice].append(len(historico))

                if b not in cores and b in vertices:
                    vertice = b
        
            if vertice == v_inicial:
                break
            else:
                vertice = historico[historico.index(vertice)-1]

        #print(v_inicial)
        #print(historico)
        v_inicial = historico[-1]

        #print(cores)
        if all(vertice in cores for vertice in vertices):
            if all(len(cores[key]) == 2 for key in cores):
                break;
        else:
            vert = vertices[0]
            for v in vertices:
                if v not in cores:
                    vertice = v
                    break;
                elif len(cores[v])<len(cores[vert]):
                    vertice = v
                    break;

    #print(cores)
    print(historico)
    #print(rem_duplicado(historico))
    print(pilha)

    return rem_duplicado(historico)

def componente_fortemente_conexo(lista_profundidade):
    componentes = []
    vertices = sorted([*lista_profundidade])
            

        
    

nome = 'grafo_D'

vertices = recebe_vertices(nome)

arestas = recebe_arestas(nome)

arestas_t = recebe_arestas_transposta(nome)

valores = recebe_valor_arestas(nome)

lista_profundidade = cria_lista_profundidade(vertices,arestas_t)

print(lista_profundidade)

busca_profundidade(lista_profundidade)       
