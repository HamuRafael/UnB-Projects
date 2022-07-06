with open("soc-dolphins.mtx",'r') as arquivo:
    grafos = []
    lines = arquivo.readlines()
    
for i in range(len(lines)) :
    grafos.append(lines[i].strip('\n'))    
for i in grafos:
    print(i)