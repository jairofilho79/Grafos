import os,time

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

def matriz_grafo(vertice,arestas,valores):
    linhas = {}
    for i in vertice:
      coluna = {}
      for j in vertice:
        if (int(i), int(j)) in arestas:
          coluna[j] = valores[arestas.index((int(i), int(j)))]
        else:
          coluna[j]  = 0;
      linhas[i] = coluna
    #print(linhas)
    return linhas

def lista_encadeada_grafo(vertices,arestas,valores):
    lista_principal = {}
    cont = 0;
    for tupla in arestas:
      lista = {}
      a,b = tupla
      lista[b] = valores[cont]
      if a not in lista_principal:
        lista_principal[a] = lista
      else:
        lista_principal[a].update(lista)
      cont+=1
    #print_lista_encadeada(lista_principal)
    return lista_principal

def matriz_mostra_adj(matriz):
    print("Adjacente de")
    for li in matriz:
        print("{}: ".format(li),end="")
        for col in matriz[li]:            
            if matriz[li][col] == 1:
               print("{} ".format(col),end="")
        print()

def lista_encadeada_mostra_adj(lista):
    print("Adjacente de")
    for li in lista:
        print("{}: ".format(li),end="")
        for col in lista[li]:
            print("{} ".format(col),end="")
        print()    

def mostrar_adjacentes(nome_estrutura,estrutura):
    print("Mostrar adjacentes do tipo "+str(nome_estrutura).replace("_"," "))
    inicio = time.time()
    globals()[nome_estrutura+'_mostra_adj'](estrutura);
    fim = time.time()
    print("Tempo para executar esta função: {}s".format(fim - inicio))
    

def main():
    grafo = 'grafo_G'
    vertices = recebe_vertices(grafo)
    arestas = recebe_arestas(grafo)
    valores = recebe_valor_arestas(grafo)
    #matriz
    #lista_encadeada
    nome_estrutura = 'lista_encadeada'
    estrutura = globals()[nome_estrutura+'_grafo'](vertices,arestas,valores)

    ''' Aqui ficam guardas as questões.
        Isso foi feito para otimizar os parâmetros (muitsa funções podem ter os mesmos parãmetros, logo, geraria muitos if: elif: desnecessários.'''
    opcoes = ["\nObrigado pela atenção!","\nDe troca vamos, então!\n",mostrar_adjacentes]

    while True:

        escolha = int(input("MENU: ({})\n0 - Sair\n1 - Trocar o Grafo\n2 - Verificar existência de arestas\n3 - Verificar se é conexo\n4 - Ver se pode ser direcionado\n".format(grafo)))

        if escolha == 0:
            print(opcoes[0])
            break

        if escolha == 1:
            print(opcoes[1])
            grafo = input("Qual o nome do grafo?\n")
            vertices = recebe_vertices(grafo)
            arestas = recebe_arestas(grafo)
            valores = recebe_valor_arestas(grafo)

        if escolha in [2]:
            opcoes[escolha](nome_estrutura,estrutura)
        
            
main()
    
        
    
