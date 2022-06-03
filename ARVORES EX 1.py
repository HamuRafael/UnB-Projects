class ArvoreBinaria:
    def __init__(self):
        self.dado = None
        self.esq = None
        self.dir = None
raiz = ArvoreBinaria()
raiz.dado = 'a'
raiz.esq = ArvoreBinaria()
raiz.esq.dado = 'b'
raiz.dir = ArvoreBinaria()
raiz.dir.dado = 'c'


def mostra(raiz):
    if raiz == None:
        print('()',end='')
    else:
        
        
        print(f'({raiz.dado}',end=' ')
        mostra(raiz.esq)
        print(' ',end='')
        mostra(raiz.dir)
        print(')',end='')
mostra(raiz)
    