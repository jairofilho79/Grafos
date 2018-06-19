import os,collections
from operator import itemgetter

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

def busca_profundidade(vertices,lista_profundidade,escolha,vertices_originais=[]):
    cores = {}
    historico = []
    pilha = []
    #print(vertices)

    
    for x in range(len(vertices)):
      vertices[x] = int(vertices[x])
      #print(vertices[x])
    #print()
    
    vertices_l_p = sorted([*lista_profundidade])

    '''
    print('oie ',end="")
    print(vertices_l_p)
    '''
    vertice = vertices[0]
    v_inicial = vertices[0]
    while True:
        while True:
            while True:
                indice_tupla = 0
                #print(vertice)
                #print(historico)
                if all(v in historico for v in vertices):
                  counter=collections.Counter(historico)
                  if min(counter.values()) >= 2:
                    if escolha == 'pilha':
                      return pilha
                    else:
                      componentes = []
                      comp = []
                      list_comps = []
                      for h in historico:
                        if h not in list_comps:
                          list_comps.append(h)
                          comp.append(h)
                        else:
                          if len(comp) != 0:
                            componentes.append(comp)
                            comp = []
                      for v in vertices_originais:
                        if v not in list_comps:
                          list_comps.append(v)
                          componentes.append([v])

                      #print(componentes)
                      return componentes
                          
                for x in range(len(lista_profundidade[vertice])):
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

                if b not in vertices_l_p and b in vertices:
                  historico.append(b)
                  if b not in pilha:
                    pilha.append(b)

                if b not in cores and b in vertices_l_p:
                    vertice = b

            '''
            if vertice not in lista_profundidade:
                while True:
                  print(historico)
                  if vertice not in historico:
                    vertice = historico[-1]
                    print(vertice)
                  else:
                    break;
            '''
            if vertice == v_inicial:
                break
            else:
              vertice = historico[historico.index(vertice)-1]
              if vertice not in lista_profundidade:
                for vert in vertices:
                  if vert not in historico:                    
                    vertice = vert
                    break
        #print(v_inicial)
        #print(historico)
        v_inicial = historico[-1]

        #print(cores)
        if all(vertice in cores for vertice in vertices_l_p):
            if all(len(cores[key]) == 2 for key in cores):                
                break;
        else:
            vert = vertices_l_p[0]
            for v in vertices_l_p:
                if v not in cores:
                    vertice = v
                    break;
                elif len(cores[v])<len(cores[vert]):
                    vertice = v
                    break;

    #print(cores)
    #print(historico)
    #print(rem_duplicado(historico))
    #print(pilha)

    return pilha
  



def componente_fortemente_conexo(vertices,lista_profundidade,arestas_t):
    #componentes = []
    #vertices = sorted([*lista_profundidade])

    pilha = busca_profundidade(vertices,lista_profundidade)

    grafo_transposto = cria_lista_profundidade(vertices,arestas_t)

    

    

        
    

nome = 'grafo_D'

vertices = recebe_vertices(nome)

arestas = recebe_arestas(nome)

arestas_t = recebe_arestas_transposta(nome)

valores = recebe_valor_arestas(nome)

lista_profundidade = cria_lista_profundidade(vertices,arestas)

#print(lista_profundidade)

pilha = busca_profundidade(vertices,lista_profundidade,'pilha')

lp_t = cria_lista_profundidade(vertices,arestas_t)

resultado = busca_profundidade(pilha,lp_t,'componentes',vertices)

resultado.sort(key=itemgetter(0))
resultado.sort(key=len)
print(resultado)
