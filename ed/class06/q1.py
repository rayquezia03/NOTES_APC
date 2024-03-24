#a pilha com arranjo tem tamanho definido
class Pilha_with_arranjo:
    topo = 0
    itens = []
    
    #inicializa a lista de itens
    def __init__(self,tamanho):
        self.itens = [None]*tamanho
        
    #inseri os itens verificando se cabe antes na lista e ja intera pro proximo topo
    def inserir(self,item):
        if self.topo < len(self.itens):
            self.itens[self.topo] = item
            self.topo += 1
        else:
            print('Erro na insercao de',item)
    
    #verifica se o topo não é zero antes de prosseguir
    def get_topo(self):
        print(self.itens[self.topo-1])
    
    def remove(self):
        if self.topo != 0:
            topo_temparario = self.topo
            self.topo -=1
            item = self.itens[self.topo] 
            return print(self.itens[topo_temparario-1]),item
        else:
            print('Erro na remocao')
            return None
        
    def imprimir(self):
        for i in range(self.topo-1,-1,-1):
            print(self.itens[i])
            
        
    
p1 = Pilha_with_arranjo(21)
palavra = 'a base do teto desaba'
original = []
for letra in palavra:
    p1.inserir((letra))
    if letra != ' ':
        original.append(letra)


palindromo = []
for i in range(0,len(palavra)):
    palindromo.append(p1.remove()[1])
    
for l in palindromo:
    if l == ' ':
        palindromo.remove(l)
        
print('########################') 
print(palindromo)

if original == palindromo:
    print("PALINDROMO")
else:
    print('NÃO')

