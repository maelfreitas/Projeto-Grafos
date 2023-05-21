import networkx as nx
import matplotlib.pyplot as plt
# Carregando a lista de vértices a partir do arquivo de texto
with open('vertices.txt', 'r') as f:
    vertices = f.read().splitlines()
# Carregando a matriz de adjacência a partir do arquivo de texto
with open('matriz.txt', 'r') as f:
    # Lendo a primeira linha que contém a informação se o grafo é direcionado ou não
    dirigido = bool(int(f.readline().strip()))
    # Lendo as demais linhas que contém a matriz de adjacência
    matriz = [[int(x) for x in line.strip().split()] for line in f]

# Criando um grafo a partir da matriz de adjacência e seus vértices
G = nx.DiGraph() if dirigido else nx.Graph()
G.add_nodes_from(vertices)
for i in range(len(vertices)):
    for j in range(len(vertices)):
        if matriz[i][j] == 1:
            G.add_edge(vertices[i], vertices[j])
# Plotando o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True) 
plt.show()
