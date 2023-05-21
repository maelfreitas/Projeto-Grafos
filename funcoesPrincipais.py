
with open("entrada.txt", "r") as f:
    entrada = f.readlines()
for i in range(len(entrada)):
    entrada[i] = entrada[i].replace(",", "")
#Verifica se o grafo é dirigido ou não
dirigido = False
if entrada[0].startswith("D"):
    dirigido = True
    entrada = entrada[1:]
elif entrada[0].startswith("ND"):
     entrada = entrada[1:]
#Extrai todos os vértices das arestas
vertices = set()
for aresta in entrada:
    v1, v2 = aresta.split()
    vertices.add(v1)
    vertices.add(v2)
#Converte o conjunto de vértices em uma lista e a ordena em ordem alfabética
vertices = sorted(list(vertices))
#Cria a matriz de adjacência
n = len(vertices)
matriz = [[0] * n for _ in range(n)]
#Preenche a matriz de adjacência
indice_vertice = {vertice: indice for indice, vertice in enumerate(vertices)}
for aresta in entrada:
    v1, v2 = aresta.split()
    indice_v1 = indice_vertice[v1]
    indice_v2 = indice_vertice[v2]
    if dirigido:
            matriz[indice_v1][indice_v2] = 1
    else:
            matriz[indice_v1][indice_v2] = 1
            matriz[indice_v2][indice_v1] = 1
print("Matriz de adjacência:")
for i in matriz:
    print(i)
input("Pressione enter para continuar\n")

def grau_vertice(matriz, vertice):
    # Encontra o índice correspondente ao vértice na matriz de adjacência
    indice = vertices.index(vertice)
    # Soma todos os elementos na linha correspondente ao vértice
    grau = sum(x for x in matriz[indice])
    return grau

vg = input("Digite o vértice que queira saber o grau:")
grau = grau_vertice(matriz, vg)
print("O grau de " + vg + " é:", end=" ")
print(grau)
input("Pressione enter para continuar\n")

def adjacentes(matriz, vertice1, vertice2):
    # Encontra os índices correspondentes aos vértices na matriz de adjacência
    indice1 = vertices.index(vertice1)
    indice2 = vertices.index(vertice2)

    if matriz[indice1][indice2] == 1:
        return True
    else:
        return False

print("Digite os vértices que queira verificar se são adjacentes:")
x = input("Primeiro vértice: ")
y = input("Segundo vértice: ")
TF = adjacentes(matriz, x, y)
if TF == True:
    print("Os vertices " + x + " e " + y + " são adjacentes!")
else:
    print("Os vertices " + x + " e " + y + " não são adjacentes!")
input("Pressione enter para continuar\n")  
  
def vizinhos(matriz, vertice):
    # Encontra o índice correspondente ao vértice na matriz de adjacência
    index = vertices.index(vertice)
    vizinhos = []
    for j in range(len(matriz)):
        if matriz[index][j] == 1:
            vizinhos.append(vertices[j])
    return vizinhos
                
v = input("Digite o vértice que queria saber os vizinhos:")
lista_vizinhos = vizinhos(matriz, v)
print(f"Vizinhos de ({v}) = {lista_vizinhos}")
input("Pressione enter para continuar\n")

print('Percorrendo as arestas')
def percorrer_arestas(matriz, vertices):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != 0:
                print(vertices[i] + " -- " + vertices[j])
percorrer_arestas(matriz, vertices)
input("Pressione enter para continuar\n")

print("Salvando grafo em arquivos .txt...\n")
def salvar_grafo(vertices, matriz, dirigido, matriz_file, vertices_file):
    # Salvando a matriz de adjacência em um arquivo de texto
    with open(matriz_file, 'w') as f:
        # Escrevendo a primeira linha indicando se o grafo é direcionado ou não
        f.write(str(int(dirigido)) + '\n')
        # Escrevendo as demais linhas com os valores da matriz
        for row in matriz:
            f.write(' '.join([str(elem) for elem in row]) + '\n') 
    # Salvando os vértices em um arquivo de texto
    with open(vertices_file, 'w') as f:
        f.write('\n'.join(sorted(vertices)))
        
salvar_grafo(vertices, matriz, dirigido, 'matriz.txt', 'vertices.txt')
print("Grafo salvo!\n")
