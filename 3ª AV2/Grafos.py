import re,os
'''
Programa desenvolvido para responder às perguntas sobre o trabalho de implementação computacional de Grafos.
Referente à disciplina Grafos, ministrada pelo Docente Prof. Dr. Nelson Neto, pela Universidade Federal do Pará.
Discentes:
Jairo Nascimento de Sousa Filho (201604940016)
Kelly (...) Costa (?)
Lucas (..) Souza (?)
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
#Funções para montar o Grafo:

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
  temp2 = []
  for i in range(0,len(temp),2):
    temp2.append("{},{}".format(temp[i],temp[i+1]))
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
    
#Funções para representar o Grafo:

def matriz_grafo(vertice,arestas,valores):
    linhas = {}
    for i in vertice:
      coluna = {}
      for j in vertice:
        if (i,j) in arestas:          
          coluna[j] = valores[arestas.index((i,j))]
        else:
          coluna[j]  = ' ';
      linhas[i] = coluna
    print_matriz(linhas)
    #return linhas

def print_matriz(linhas):
    print(end="  ")
    for linha in linhas:
      print(linha,end=" ")
    print()
    for linha in linhas:
      print(linha,end=" ")
      for col in linhas[linha]:
        print(linhas[linha][col], end=" ")
      print()

''' É a mesma coisa do existe_aresta(), só o nome que difere.
    Estou até pensando em tirar.
    Até porque, nessa implementação (utilizando hashing keys) tanto a lista de adjacência como a matriz tem a mesma forma de encontrar a aresta.'''
def existe_aresta_matriz(linhas):
    while True:
        resposta = input("Insira a aresta no formato: i j (i espaço j). Insira 0 para sair.\n")

        if resposta != '0':
          
            if func_existe_aresta(resposta,linhas):
                print("Verdadeiro!\n")
            else:
                print("Falso!\n")
        else:
            break
          
def lista_encadeada_grafo(arestas,valores):
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
    print_lista_encadeada(lista_principal)
    #return lista_principal

def print_lista_encadeada(lista_principal):
      for lista in lista_principal:
        print(lista,end=" ")
        for l in lista_principal[lista]:
          print("| {}:{} |".format(l,lista_principal[lista][l]), end=" ")
        print()

''' É a mesma coisa do existe_aresta(), só o nome que difere.
    Estou até pensando em tirar.
    Até porque, nessa implementação (utilizando hashing keys) tanto a lista de adjacência como a matriz tem a mesma forma de encontrar a aresta.'''
def existe_aresta_lista_encadeada(lista_principal):
    while True:
        resposta = input("Insira a aresta no formato: i j (i espaço j). Insira 0 para sair.\n")

        if resposta != '0':
          
            if func_existe_aresta(resposta,lista_principal):
                print("Verdadeiro!\n")
            else:
                print("Falso!\n")
        else:
            break
        

#Funções de operações sobre o Grafo:
''' Eu quero criar uma função para cada questão.
    Tipo: def questao_1(): #chama-se todas as funções e todo o algoritmo necessário para fazer a 1ª questão.
    Talvez seja por isso que eu esteja demorando, porque estou fazendo as funções serem genéricas.'''
def aumentar_num_vertices(vertices, arestas, valores):
    #print("Falta fazer")
    #Deve pedir um determinado número de novos vértices e pedir que cada um destes se liguem a dois outros vértices. Deve-se salvar como grafo atual.

    nome_grafo = input("Qual o nome do grafo?\n")

    num_new_vertice = int(input("Quantos novos vértices?\n"))
    
    for i in range(num_new_vertice):
      while True:
        vertice = input("Insira o Vértice\n")
        if vertice not in vertices:
          vertices.append(vertice)
          while True:
            aresta1 = input("Insira a aresta 1 no formato: i j (i espaço j).\n")
            ij = aresta1.split(' ')
            if ij[0] == vertice or ij[1] == vertice:
              if not (ij[0],ij[1]) in arestas:
                arestas.append((ij[0],ij[1]))
                valores.append(input("Insira o valor da aresta\n"))
                break;
              else:
                print("Essa aresta já existe, por favor, coloque outra.")
            else:
              print("Você não está conectando o novo vértice.")
          while True:
            aresta2 = input("Insira a aresta 2 no formato: i j (i espaço j).\n")
            ij = aresta2.split(' ')
            if ij[0] == vertice or ij[1] == vertice:
              if not (ij[0],ij[1]) in arestas:
                arestas.append((ij[0],ij[1]))
                valores.append(input("Insira o valor da aresta\n"))
                break;
              else:
                print("Esta aresta já existe, por favor, coloque outra.")
            else:
              print("Você não está conectando o novo vértice.")
          else:
            print("Este vértice já existe!")
          break;  

    ''' Isso aqui está com problemas, ainda estou trabalhando para resolver! '''
    #Salvar Vertice
    pasta_nova = os.path.dirname(os.path.realpath(__file__))
    arq2 = open(pasta_nova+'\\Grafos\\'+nome_grafo+'.txt','w')
    for i in range(len(vertices)-1):
        arq2.write("{},".format(vertices[i]))
    arq2.write("{}".format(vertices[-1]))
    arq2.write("\n")
    arq2.close()

    #Salvar Aresta
    arq3 = open(pasta_nova+'\\Grafos\\'+nome_grafo+'.txt','a')
    for j in range(len(arestas)):
      arestas[j] = str(arestas[j]).replace(" ","")
    for i in range(0,len(arestas)-2,2):
        arq3.write("{},{},".format(arestas[i],arestas[i+1]))
    arq3.write("{},{}".format(arestas[-2],arestas[-1]))
    arq3.write("\n")
    arq3.close()

    #Salvar Valor da aresta    
    arq4 = open(pasta_nova+'\\Grafos\\'+nome_grafo+'.txt','a')
    for i in range(len(valores)-1):
        if is_int(valores[i]):
            arq4.write("{},".format(int(valores[i])))
        elif is_float(valores[i]):
            arq4.write("{},".format(float(valores[i])))
        else:
            arq4.write("{},".format(valores[i]))
    arq4.write("{}".format(valores[-1]))
    arq4.write("\n")
    arq4.close()
    
    return nome_grafo

def gerar_grafo_completo(vertices):
    print("Falta fazer")
    nome_grafo = 'grafo_M';
    
    #Salvar Vertice
    pasta_nova = os.path.dirname(os.path.realpath(__file__))
    arq2 = open(pasta_nova+'\\Grafos\\'+nome_grafo+'.txt','w')
    for i in range(len(vertices)-1):
        arq2.write("{},".format(vertices[i]))
    arq2.write("{}".format(vertices[-1]))
    arq2.write("\n")
    arq2.close()

    cont = 0
    #Salvar Aresta
    arq3 = open(pasta_nova+'\\Grafos\\'+nome_grafo+'.txt','a')
    for vertice1 in vertices:
      for vertice2 in vertices:
        if vertice1 == vertices[-1] and vertice2 == vertices[-1]:
            arq3.write("({},{})".format(vertice1,vertice2))
            break;
        if vertice1 == vertice2:
          continue;
        arq3.write("({},{}),".format(vertice1,vertice2))
        cont+=1
    arq3.write("\n")      
    arq3.close()
    #Salvar Valor da aresta    
    arq4 = open(pasta_nova+'\\Grafos\\'+nome_grafo+'.txt','a')
    for i in range(cont):
        arq4.write("{},".format(1))
    arq4.write("{}".format(1))
    arq4.write("\n")
    arq4.close()
    

    
    #Deve-se criar dois for e cada vértice, ignorando a si mesmos.

    


    
''' As funções são divididas em: a função propriamente dita, que retorna o valor pedido pelo professor;
    e a parte funcional da função, a que retorna verdadeiro ou falso.
    Por isso será muito comundo encontrar:
    def func_alguma_coisa():
    def alguma_coisa():'''

def func_existe_aresta(aresta,arestas):
    ij = aresta.split(' ')
    return True if (ij[0],ij[1]) in arestas else False


def existe_aresta(arestas):
    while True:
        resposta = input("Insira a aresta no formato: i j (i espaço j). Insira 0 para sair.\n")

        if resposta != '0':
          
            if func_existe_aresta(resposta,arestas):
                print("Verdadeiro!\n")
            else:
                print("Falso!\n")
        else:
            break

    

def main():
    grafo = 'grafo_G'
    vertices = recebe_vertices(grafo)
    arestas = recebe_arestas(grafo)
    valores = recebe_valor_arestas(grafo)

    ''' Aqui ficam guardas as questões.
        Isso foi feito para otimizar os parâmetros (muitsa funções podem ter os mesmos parãmetros, logo, geraria muitos if: elif: desnecessários.'''
    opcoes = ["\nObrigado pela atenção!","\nDe troca vamos, então!\n",existe_aresta]

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
            opcoes[escolha](arestas)
        elif escolha in [3]: #Opção para testes, por enquanto. Visto que estava testando bastante as questões de produzir o grafo através do arquivo, para ser uma matriz etc.
          #aumentar_num_vertices(vertices,arestas,valores)
          gerar_grafo_completo(vertices)
            
main()
