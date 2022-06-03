x=0
lista_songs=[]
f=0
current_song = ''

salvos=[]
lista2=[]
while True:
        x = input()
        salvos.append(x)
        
        if x.startswith('add'):
            x,y=x.split()
            lista_songs.append(y)
            lista2.append(y)
            salvos.append('add')
            
        if x.startswith('del'):
            x,y=x.split()
            if current_song == y:
                break
            else:    
                lista_songs.remove(y)
                lista2.remove(y)
                salvos.append('del')
        if x.startswith('next'):
            salvos.append('next')
            x,y=x.split()
            if len(lista_songs) >= 1:
                if current_song == '':
                    lista_songs.insert(0,y)
                if current_song != y:
                    lista_songs.insert(1,y)
                    
                       
        #COMEÇA AS PALAVRAS CHAVE#
        if x == 'undo':
            if  'add' in salvos:
                lista_songs.pop(len(lista_songs) - 1)
                salvos.remove('add')
            if 'del' in salvos:
                lista_songs.append(y)
                salvos.remove('del')
            if 'next' in salvos:
                lista_songs = lista2
                salvos.remove('next')
                
            
        if x == 'undo *': 
            lista_songs=[]
        if x == 'play':
            current_song = lista_songs[0]
        if x=='stop':
            if 'play' in salvos:
                current_song = ''
            
        if x == 'ended':
            if 'play' in salvos:
                for i in lista2:
                    
                    current_song = i
                    break
                    
                lista2.pop(0)
                lista_songs.pop(0)
                salvos.remove('play')
            if 'play' in salvos:
                
                for i in lista2:
                    current_song=i
                    break
          
        if x == 'list':
            if lista_songs ==[]:
                print('[vazia]')
            else:
                lista = [str(a) for a in lista_songs]
                print(','.join(lista))
           
                
        if x=='current':
            if lista_songs == []:
                print('Toque! Toque, Dijê!')
            
            elif current_song == '':
                print(lista_songs[0])
            else:
                print(current_song)
        if x== 'fight':
            print('Jedi Wagner, assuma o comando!')
            break  
            
        
            
    