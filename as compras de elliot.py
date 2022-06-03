class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
lista=[]
lista2=[]
s=Stack()
while True:
    try:
        
        x,y=input().split()
        if x =='-':
            for i in lista:
                if i[0]== y:
                    lista.remove(i)
                    
        else:
            y= float(y)
            lista.append((x,y))
    
        
            
            
            
    except ValueError:
        for i in lista:
            s.push(i)
        for i in lista:
            
            lista2.append(s.pop())
        break
total=0
for i in lista2:    
    total += i[1]
    print(f'{i[0]}: R$ {i[1]:.2f}')
    
        
print('----------------------')
print(f'{len(lista)} item(ns): R${total:.2f}')
    
    
    