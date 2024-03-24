class PilhaArranjo:
    topo = 0
    itens = []
    
    def __init__(self,capacidade):
        self.itens = [None]*capacidade
        
    def empilhar(self,item):
        if self.topo < len(self.itens):
            self.itens[self.topo] = item
            self.topo +=1
        else:
            print("erro ao empilhar o seguinte item", item)
            
    def desempilhar(self):
        if self.topo != 0:
            self.topo -=1
            item = self.itens[self.topo]
            return item
        else:
            print("erro ao desempilhar o item")
            
    def imprimir(self):
        for i in range(self.topo-1,-1,-1):
            print(self.itens[i])
            
p1 = PilhaArranjo(10)
print(p1)
# p1.imprimir()
p1.empilhar((1,'google.com'))
p1.empilhar((2,'ava.ead.ufal.br'))
# p1.inserir((3,'sistemas.ufal.br'))
# p1.inserir((4,'instagram.com'))
# p1.inserir((5,'instagram.com'))
# p1.inserir((6,'instagram.com'))
p1.imprimir()
p1.desempilhar()



# p1.remover()
print('@@@@@@@@@@@@@@@@@@@@22')
p1.imprimir()
