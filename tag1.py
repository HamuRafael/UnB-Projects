class Grafo:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]
    def adiciona_arestas(self,u,v):
        self.grafo[u-1].append(v)
        self.grafo[v-1].append(u)

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:',end=' ')
            for j in self.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')            
        
g = Grafo(62)
graph_updated = []

with open("soc-dolphins.mtx",'r') as arquivo: #le o arquivo ge grafos
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
