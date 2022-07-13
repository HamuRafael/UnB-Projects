class Grafo:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
    def adiciona_arestas(self,u,v):
        self.grafo[u-1].append(v)
        self.grafo[v-1].append(u)

    def mostra_lista(self):
        for i in range(self.vertices):
            lista_test = []
            
            for j in self.grafo[i]:
                lista_test.append(j)  

            lista_adjacencia.append(lista_test)
        print(f'{lista_adjacencia}')
def BronKerbosch_sem_pivoteamento(P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from BronKerbosch_sem_pivoteamento(
            P.intersection(grafo[v]), R.union([v]), X.intersection(grafo[v]))
        X.add(v)


g = Grafo(62)
graph_updated = []
lista_adjacencia = []
lista_test = []
with open("soc-dolphins.mtx",'r') as arquivo: #le o arquivo de grafos
    grafos = []
    lines = arquivo.readlines()
  
for i in range(len(lines)) :
    grafos.append(lines[i].strip('\n'))    #strip '\n'
grafos = [grafos.replace(' ',',')for grafos in grafos]
for i in grafos:
    
    splitado = i.split(',')
    graph_updated.append(splitado)
graph_updated = [list(map(int, x)) for x in graph_updated]


for i in graph_updated:
    g.adiciona_arestas(i[0],i[1])
g.mostra_lista()

