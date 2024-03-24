class Pilha:
    itens = []
    topo = 0

    def __init__(self,tamanho):
        self.itens = [None]*tamanho
        
    def inserir(self,item):
        if self.topo < len(self.itens):
            self.itens[self.topo] = item
            self.topo += 1
        else:
            print('Erro na insercao de',item)
        
    def remover(self):
        if self.topo != 0:
            self.topo -= 1
            item = self.itens[self.topo]
            return item 
        else:
            print('Erro na remocao')
            return None
    
    def imprimir(self):
        for i in range(self.topo-1,-1,-1):
            print(self.itens[i])

p1 = Pilha(10)
print(p1)
# p1.imprimir()
p1.inserir((1,'google.com'))
p1.inserir((2,'ava.ead.ufal.br'))
# p1.inserir((3,'sistemas.ufal.br'))
# p1.inserir((4,'instagram.com'))
# p1.inserir((5,'instagram.com'))
# p1.inserir((6,'instagram.com'))
p1.imprimir()


# p1.remover()
print('@@@@@@@@@@@@@@@@@@@@22')
p1.imprimir()

# p1.remover()
# p1.imprimir()

# p1.remover()
# p1.remover()
# p1.remover()
# p1.remover()
# p1.remover()