nome =input('Qual seu nome? :')
print(f'Bem vindo(a) {nome}')
print()
print('Fala pra nós a sua lista ai vai...')
print('Por favor, cada nome em uma linha para não bugar o programa =)')

x = 0

xis=0
lista =[]
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
ai=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
y=0
z=0

while x != 'sair':
    
        x=input()
        if x == 'sair':
            break
        else:
        
            lista.append(x)
for i in lista:
    if i.startswith('a') == True:
        a+=1
    elif i.startswith('b') == True:
        b+=1
    elif i.startswith('c') == True:
        c+=1  
    elif i.startswith('d') == True:
        d+=1  
    elif i.startswith('e') == True:
        e+=1
    elif i.startswith('f') == True:
        f+=1
    elif i.startswith('g') == True:
        g+=1
    elif i.startswith('h') == True:
        h+=1
    elif i.startswith('i') == True:
        ai+=1    
    elif i.startswith('j') == True:
        j+=1
    elif i.startswith('k') == True:
        k+=1
    elif i.startswith('l') == True:
        l+=1
    elif i.startswith('m') == True:
        m+=1
    elif i.startswith('n') == True:
        n+=1
    elif i.startswith('o') == True:
        o+=1
    elif i.startswith('p') == True:
        p+=1
    elif i.startswith('q') == True:
        q+=1
    elif i.startswith('r') == True:
        r+=1
    elif i.startswith('s') == True:
        s+=1
    elif i.startswith('t') == True:
        t+=1
    elif i.startswith('u') == True:
        u+=1
    elif i.startswith('v') == True:
        v+=1
    elif i.startswith('x') == True:
        xis+=1
    elif i.startswith('w') == True:
        w+=1
    elif i.startswith('y') == True:
        y+=1
    elif i.startswith('z') == True:
        z+=1
        
    
print(f'Voce beijou {len(lista)} pessoas.')

print(f'A = {a}')
print(f'B = {b}')
print(f'C = {c}')
print(f'D = {d}')
print(f'E = {e}')
print(f'F = {f}')
print(f'G = {g}')
print(f'H = {h}')
print(f'I = {ai}')
print(f'J = {j}')
print(f'K = {k}')
print(f'L = {l}')
print(f'M = {m}')
print(f'N = {n}')
print(f'O = {o}')
print(f'P = {p}')
print(f'Q = {q}')
print(f'R = {r}')
print(f'S = {s}')
print(f'T = {t}')
print(f'U = {u}')
print(f'V = {v}')
print(f'X = {xis}')
print(f'W = {w}')
print(f'Y = {y}')
print(f'Z = {z}')


    