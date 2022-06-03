T,N=input().split()
T,N=int(T),int(N)
variavel = 0
variavel2=0
lista_atributo = ['bison', 'elephant', 'horse', 'ibis', 'sky', 'mountain', 'building', 'flower', 'sand', 'tree', 'field', 'road', 'tower', 'ocean', 'cliff', 'waterfall']
n=1
a1= 0
a2=0



lista_numero =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
import math
if T == 1:
    while n <= N:
        pular_linha=input()
        nome_do_arquivo=str(input())
        atributo_objeto=str(input())
        x1,y1,x2,y2=input().split()
        x1,y1,x2,y2=float(x1),float(y1),float(x2),float(y2)
        if variavel2== 0: 
            variavel2 += 1
            variavel = nome_do_arquivo
        if variavel != nome_do_arquivo:
            print(variavel +' ' + ' '.join(map(str, lista_numero))) 
            for i in range(16):
                variavel = nome_do_arquivo
                lista_numero =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
        if variavel == nome_do_arquivo:
            for i in range(16):
                if lista_atributo[i] in atributo_objeto:
                    lista_numero[i] = 1
        n+=1            
    print(variavel +' ' + ' '.join(map(str, lista_numero)))            
    
        
elif T == 2 :
    
    variavel = 0
    listaarquivos = []
    listacaixas = []
    listax = []
    listay = []
    lista_largura = []
    lista_altura = []
    lista_area = []
    lista_desvio_x = []
    lista_desvio_y = []
    lista_desvio_largura = []
    lista_desvio_altura = []
    
    for i in range(N):
        pular_linha=input()
        nome_do_arquivo=str(input())
        atributo_objeto=str(input())
        x1,y1,x2,y2=input().split()
        x1,y1,x2,y2=float(x1),float(y1),float(x2),float(y2)
        listaarquivos.append(nome_do_arquivo)
        
        if variavel == nome_do_arquivo or variavel == 0:
            listacaixas.append(nome_do_arquivo)
            listax.append((x2+x1)/2)
            listay.append((y2+y1)/2)
            lista_largura.append(x2-x1)
            lista_altura.append(y2-y1)
            lista_area.append((x2-x1)*(y2-y1))
            listaarquivos.append(nome_do_arquivo)
            variavel = nome_do_arquivo
        
        elif variavel != nome_do_arquivo or set(lista_arquivo) == 1:
            q1 = len(listacaixas) / 2 
            q2 = (sum(listax) / len(listax)) / 128
            q3 = (sum(listay) / len(listay)) / 128
            q4 = (sum(lista_largura) / len(lista_largura)) / 128
            q5 = (sum(lista_altura) / len(lista_altura)) / 128
            q6 = (sum(lista_area) / len(lista_area)) / (128**2)
            
            for i in listax:
                lista_desvio_x.append((i-(sum(listax) / len(listax)))**2)
            for j in listay:
                lista_desvio_y.append((j-(sum(listay) / len(listay)))**2)
            for m in lista_largura:
                lista_desvio_largura.append((m-(sum(lista_largura) / len(lista_largura)))**2)
            for l in lista_altura:
                lista_desvio_altura.append((l-(sum(lista_altura) / len(lista_altura)))**2)
            
            q7 = ((sum(lista_desvio_x) / len(listax))**(1/2)) / 32
            q8 = ((sum(lista_desvio_y) / len(listay))**(1/2)) / 32
            q9 = ((sum(lista_desvio_largura) / len(lista_largura))**(1/2)) / 32
            q10 = ((sum(lista_desvio_altura) / len(lista_altura))**(1/2)) / 32
            print(f'{variavel} {q1:.1f} {q2:.1f} {q3:.1f} {q4:.1f} {q5:.1f} {q6:.1f} {q7:.1f} {q8:.1f} {q9:.1f} {q10:.1f}')
            
            variavel = nome_do_arquivo
            
            listacaixas = []
            listax = []
            listay = []
            lista_largura = []
            lista_altura = []
            lista_area = []
            lista_desvio_x = []
            lista_desvio_y = []
            lista_desvio_largura = []
            lista_desvio_altura = []
            listacaixas.append(nome_do_arquivo)
            listax.append((x2+x1)/2)
            listay.append((y2+y1)/2)
            lista_largura.append(x2-x1)
            lista_altura.append(y2-y1)
            lista_area.append((x2-x1)*(y2-y1))
            listaarquivos.append(nome_do_arquivo)
            variavel = nome_do_arquivo
    else:
        q1 = len(listacaixas) / 2
        q2 = (sum(listax) / len(listax)) / 128
        q3 = (sum(listay) / len(listay)) / 128
        q4 = (sum(lista_largura) / len(lista_largura)) / 128
        q5 = (sum(lista_altura) / len(lista_altura)) / 128
        q6 = (sum(lista_area) / len(lista_area)) / (128**2)
            
        for i in listax:
            lista_desvio_x.append((i-(sum(listax) / len(listax)))**2)
        for j in listay:
            lista_desvio_y.append((j-(sum(listay) / len(listay)))**2)
        for k in lista_largura:
            lista_desvio_largura.append((k-(sum(lista_largura) / len(lista_largura)))**2)
        for l in lista_altura:
            lista_desvio_altura.append((l-(sum(lista_altura) / len(lista_altura)))**2)
            
        q7 = ((sum(lista_desvio_x) / len(listax))**(1/2)) / 32
        q8 = ((sum(lista_desvio_y) / len(listay))**(1/2)) / 32
        q9 = ((sum(lista_desvio_largura) / len(lista_largura))**(1/2)) / 32
        q10 = ((sum(lista_desvio_altura) / len(lista_altura))**(1/2)) / 32
        
        print(f'{variavel} {q1:.1f} {q2:.1f} {q3:.1f} {q4:.1f} {q5:.1f} {q6:.1f} {q7:.1f} {q8:.1f} {q9:.1f} {q10:.1f}')
        
        '''lista_altura.append(x2-x1)
        #xmed+=x1+x2
        #ymed+=y1+y2
        #area += ((x2-x1) * (y2-y1))
        #largura_media+= x2-x1
        #altura_media+=y2-y1
        #xmed_d = math.sqrt(((x1-(xmed/(2*N)))**2 + (x2-(xmed/(2*N)))**2)/2)  
       # ymed_d = math.sqrt(((y1-(ymed/(2*N)))**2 + (y2-(ymed/(2*N)))**2)/2)## 
        
        #if variavel2== 0: 
            #variavel2 += 1
            #variavel = nome_do_arquivo    
        #if variavel == nome_do_arquivo:
        #if variavel != nome_do_arquivo:'''
if T==3:
    for i in range(N):
        variavel_1 = 0
        variavel = 0
        listaarquivos = []
        listacaixas = []
        listax = []
        listay = []
        lista_largura = []
        lista_altura = []
        lista_area = []
        lista_desvio_x = []
        lista_desvio_y = []
        lista_desvio_largura = []
        lista_desvio_altura = []
    
        pular_linha=input()
        nome_do_arquivo=str(input())
        atributo_objeto=str(input())
        x1,y1,x2,y2=input().split()
        x1,y1,x2,y2=float(x1),float(y1),float(x2),float(y2)
        listaarquivos.append(nome_do_arquivo)
        if variavel2== 0: 
            variavel2 += 1
            variavel_1 = nome_do_arquivo
        if variavel_1 != nome_do_arquivo:
            print(variavel_1 +' ' + ' '.join(map(str, lista_numero))) 
            for i in range(16):
                variavel_1 = nome_do_arquivo
                lista_numero =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
        if variavel_1 == nome_do_arquivo:
            for i in range(16):
                if lista_atributo[i] in atributo_objeto:
                    lista_numero[i] = 1
    
     
        if variavel == nome_do_arquivo or variavel == 0:
            listacaixas.append(nome_do_arquivo)
            listax.append((x2+x1)/2)
            listay.append((y2+y1)/2)
            lista_largura.append(x2-x1)
            lista_altura.append(y2-y1)
            lista_area.append((x2-x1)*(y2-y1))
            listaarquivos.append(nome_do_arquivo)
            variavel = nome_do_arquivo
        
        elif variavel != nome_do_arquivo or set(lista_arquivo) == 1:
            q1 = len(listacaixas) / 2 
            q2 = (sum(listax) / len(listax)) / 128
            q3 = (sum(listay) / len(listay)) / 128
            q4 = (sum(lista_largura) / len(lista_largura)) / 128
            q5 = (sum(lista_altura) / len(lista_altura)) / 128
            q6 = (sum(lista_area) / len(lista_area)) / (128**2)
            
            for i in listax:
                lista_desvio_x.append((i-(sum(listax) / len(listax)))**2)
            for j in listay:
                lista_desvio_y.append((j-(sum(listay) / len(listay)))**2)
            for m in lista_largura:
                lista_desvio_largura.append((m-(sum(lista_largura) / len(lista_largura)))**2)
            for l in lista_altura:
                lista_desvio_altura.append((l-(sum(lista_altura) / len(lista_altura)))**2)
            
            q7 = ((sum(lista_desvio_x) / len(listax))**(1/2)) / 32
            q8 = ((sum(lista_desvio_y) / len(listay))**(1/2)) / 32
            q9 = ((sum(lista_desvio_largura) / len(lista_largura))**(1/2)) / 32
            q10 = ((sum(lista_desvio_altura) / len(lista_altura))**(1/2)) / 32
            print(f'{variavel} {q1:.1f} {q2:.1f} {q3:.1f} {q4:.1f} {q5:.1f} {q6:.1f} {q7:.1f} {q8:.1f} {q9:.1f} {q10:.1f}')
            
            variavel = nome_do_arquivo
            
            listacaixas = []
            listax = []
            listay = []
            lista_largura = []
            lista_altura = []
            lista_area = []
            lista_desvio_x = []
            lista_desvio_y = []
            lista_desvio_largura = []
            lista_desvio_altura = []
            listacaixas.append(nome_do_arquivo)
            listax.append((x2+x1)/2)
            listay.append((y2+y1)/2)
            lista_largura.append(x2-x1)
            lista_altura.append(y2-y1)
            lista_area.append((x2-x1)*(y2-y1))
            listaarquivos.append(nome_do_arquivo)
            variavel = nome_do_arquivo
    else:
        q1 = len(listacaixas) / 2
        q2 = (sum(listax) / len(listax)) / 128
        q3 = (sum(listay) / len(listay)) / 128
        q4 = (sum(lista_largura) / len(lista_largura)) / 128
        q5 = (sum(lista_altura) / len(lista_altura)) / 128
        q6 = (sum(lista_area) / len(lista_area)) / (128**2)
            
        for i in listax:
            lista_desvio_x.append((i-(sum(listax) / len(listax)))**2)
        for j in listay:
            lista_desvio_y.append((j-(sum(listay) / len(listay)))**2)
        for k in lista_largura:
            lista_desvio_largura.append((k-(sum(lista_largura) / len(lista_largura)))**2)
        for l in lista_altura:
            lista_desvio_altura.append((l-(sum(lista_altura) / len(lista_altura)))**2)
            
        q7 = ((sum(lista_desvio_x) / len(listax))**(1/2)) / 32
        q8 = ((sum(lista_desvio_y) / len(listay))**(1/2)) / 32
        q9 = ((sum(lista_desvio_largura) / len(lista_largura))**(1/2)) / 32
        q10 = ((sum(lista_desvio_altura) / len(lista_altura))**(1/2)) / 32
        
        print(f'{variavel} {q1:.1f} {q2:.1f} {q3:.1f} {q4:.1f} {q5:.1f} {q6:.1f} {q7:.1f} {q8:.1f} {q9:.1f} {q10:.1f}')
    print(variavel_1 +' ' + ' '.join(map(str, lista_numero)))

    
            
            
        
        
    
            
            
            
       

    
    
    
               