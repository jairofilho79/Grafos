import os;

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

nome_grafo = input("Qual o nome do grafo?\n")

vertices = []
arestas  = []
valores  = []

while True:
  vertice = input("Insira o vértice (digite 'p' para parar)\n")
  if vertice != 'p':
    vertice = int(vertice)
    if vertice not in vertices:
      vertices.append(vertice)      
    else:
      print("Este vértice já existe!")
  else:
    break


while True:
  ij = input("Insira a aresta no formato: i j (i espaço j) (digite 'p' para parar).\n").split(' ')
  if ij[0] != 'p':
    if int(ij[0]) in vertices and int(ij[1]) in vertices:
      if not (int(ij[0]),int(ij[1])) in arestas:
        arestas.append((int(ij[0]),int(ij[1])))
        valores.append(float(input("Insira o valor da aresta\n")))
      else:
        print("Essa aresta já existe, por favor, coloque outra.")
    else:
      print("Você está conectando vértice inválido")
  else:
    break;
          
#Salvar Vertice
if len(vertices) != 0:
  pasta_nova = os.path.dirname(os.path.realpath(__file__))
  arq2 = open(pasta_nova+'\\Grafos\\'+nome_grafo+'.txt','w')
  for i in range(len(vertices)-1):
      arq2.write("{},".format(vertices[i]))
  arq2.write("{}".format(vertices[-1]))
  arq2.write("\n")
  arq2.close()

#Salvar Aresta
if len(arestas) != 0:
  arq3 = open(pasta_nova+'\\Grafos\\'+nome_grafo+'.txt','a')
  for j in range(len(arestas)):
    arestas[j] = str(arestas[j]).replace(" ","")
  for i in range(len(arestas)-1):
      r,t = eval(arestas[i])
      arq3.write("({},{}),".format(r,t))

  r,t = eval(arestas[len(arestas)-1])
  arq3.write("({},{})".format(r,t))
  arq3.write("\n")
  arq3.close()


#Salvar Valor da aresta
if len(valores) != 0:
  arq4 = open(pasta_nova+'\\Grafos\\'+nome_grafo+'.txt','a')
  for i in range(len(valores)-1):
      if is_int(valores[i]):
          arq4.write("{},".format(int(valores[i])))
      elif is_float(valores[i]):
          arq4.write("{},".format(float(valores[i])))
      else:
          arq4.write("{},".format(valores[i]))
  if len(arestas) != 0:
    if is_int(valores[i]):
          arq4.write("{}".format(int(valores[i])))
      elif is_float(valores[i]):
          arq4.write("{}".format(float(valores[i])))
      else:
          arq4.write("{}".format(valores[i]))
  arq4.write("\n")
  arq4.close()

print("Grafo gerado com sucesso!")
