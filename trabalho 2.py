class ArvoreBinaria:
    def __init__(self):
        self.dado = None
        self.esq = None
        self.dir = None
raiz = ArvoreBinaria()
def add(raiz, value, string,i=0):
    if len(string) > i:
        
        if string[i] == '.':
            i+=1
            if raiz.esq == None:
                no = ArvoreBinaria()
                raiz.esq = no
                
            add(raiz.esq,value,string,i)
           
        elif string[i] == '-':
            i+=1
            if raiz.dir == None:
                no = ArvoreBinaria()
                raiz.dir = no
            add(raiz.dir,value,string,i)
            
    else:
        raiz.dado = value
def nivel(value):
    fila=[]
    fila.append(value)
    while len(fila) !=0:
        raiz=fila.pop(0)
        if raiz.dado == None:
            print('*',end=' ')
        else:
            
            print(raiz.dado,end=' ')
        if raiz.esq is not None:
            fila.append(raiz.esq)
        if raiz.dir is not None:
            fila.append(raiz.dir)
        
    
    
    
      

x = int(input())
dic_morse = {'/':' '}
dic_alf = {'' : '/'}
n=0
lista = [' ']
listacode=[' ']
l=0
while n < x:
    value,string = input().split()
    lista.append(value)
    listacode.append(string)
    add(raiz,value,string,0)
    
    dic_morse.update({string : value})
    dic_alf.update({value : string})
    n+=1
valor = int(input())
if valor == 0:
    palavra = input().split()
if valor == 1:
    palavra = input()


def palavra_to_morse(palavra): #1#
    for i in palavra:
        if i not in lista:
            global l
            l = 1
            print('Impossível codificar a mensagem!',end='')
            break
            
        
    for i in range(0, len(palavra)):
        if l ==1 :
            break
        elif palavra[i] in dic_alf or palavra[i] == ' ':
            
                                  
            if palavra[i] == ' ' and palavra[i] != palavra[i-1]:
                print('/',end='')
                
            else:
                if palavra[i] == ' ':
                    continue
                else:
                
                    print(dic_alf.get(palavra[i]),end=' ')
        else:
            if palavra[i] == ' ':
                print('/',end='')
        
            continue

def morse_to_palavra(palavra): #0#
    for i in range(0, len(palavra)):
        if palavra[i] not in listacode and True !=palavra[i].startswith('/'):
            global l
            l = 1
            print('Impossível decodificar a mensagem!',end='')
            break
            
        
        if palavra[i].startswith('/') and l!=1:
            print(' ',end='')
            new_word=palavra[i].replace('/','')
            print(dic_morse.get(new_word),end='')
            
        else:
        
            print(dic_morse.get(palavra[i]),end='')   

if valor == 1:
    palavra_to_morse(palavra)
if valor == 0:
    morse_to_palavra(palavra)
def mostra(raiz):
    if raiz == None:
        print('()',end='')
    else:
        if raiz.dado == None:
            print('(*',end= ' ')
        else:
            
            print(f'({raiz.dado}',end=' ')
        mostra(raiz.esq)
        print(' ',end='')
        mostra(raiz.dir)
        print(')',end='')
#mostra(raiz)
print('')
g=1

# if l == 1:
    #g+=1
#else:
    
    #nivel(raiz)




    
    


