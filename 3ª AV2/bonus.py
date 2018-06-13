def func_is_conexo(vertices,arestas):
    conjunto_vertice = []

    for aresta in arestas: 
      for a in aresta:
        conjunto_vertice.append(a)

    conjunto_vertice = set(conjunto_vertice)
    for vertice in vertices:
        if vertice not in conjunto_vertice:
            return False
    return True

def is_conexo(vertices,arestas):
    print(vertices)
    print(arestas)
    if func_is_conexo(vertices,arestas):
        print("O Grafo é conexo!\n")
    else:
        print("O Grafo não é conexo!\n")
        
def func_is_biconexo(arestas):
  
    print("Falta terminar")
    #Retirar uma aresta por vez e verificar se ainda é conexo
    for a in range(len(arestas)):
      tem = arestas.pop(0)
      if not func_is_conexo(arestas):
        return False
      arestas.append(tem)
    return True

def is_biconexo(arestas):
    
    if func_is_biconexo(arestas):
      print("É Biconexo")
    else:
      print("Não é Biconexo")

def func_is_direcionado(arestas):
    #print(arestas)
    for aresta in arestas:
        a,b = aresta
        if (b,a) not in arestas:
            return False            
    return True

def is_direcionado(arestas):

    if func_is_direcionado(arestas):
        print("Pode ser direcionado\n");
    else:
        print("Não pode ser direcionado\n")

def there_is_ponto_de_articulacao():
    print("Falta fazer")
    #Retirar todas arestas que contém o vértice, um por vez, e verificar se ainda é conexo

def unilateral_conexo():
    print("Falta fazer")

def forte_conexo():
    print("Falta fazer")

def valor_grau():
    print("Falta fazer")
    #Contabilizar quantas vezes o vértice aparece na lista de arestas, se for direcionado (perguntar ao usuário), dividir esse valor por 2.

def main():
    grafo = 'grafo_H'
    vertices = recebe_vertices(grafo)
    arestas = recebe_arestas(grafo)
    valores = recebe_valor_arestas(grafo)
    escolha = -1

    ''' Aqui ficam guardas as questões.
        Isso foi feito para otimizar os parâmetros (muitsa funções podem ter os mesmos parãmetros, logo, geraria muitos if: elif: desnecessários.'''
    opcoes = ["\nObrigado pela atenção!","\nDe troca vamos, então!\n",existe_aresta,is_conexo,is_direcionado]

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

        if escolha in [2,4]:
            opcoes[escolha](arestas)
        elif escolha in [3]:
            opcoes[escolha](vertices,arestas)
        elif escolha in [5]: #Opção para testes, por enquanto. Visto que estava testando bastante as questões de produzir o grafo através do arquivo, para ser uma matriz etc.
          aumentar_num_vertices(vertices,arestas,valores)
