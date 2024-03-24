class Lista:
    tamanho = 0
    itens = None
    fim = 0

    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.itens = [None]*tamanho

    def inserirPos(self,pos,item):
        if self.fim < self.tamanho and abs(pos) <= self.fim:
            self.itens[pos] = item
            if pos == self.fim:
                self.fim+=1
        else:
            print('posição inválida')

    def append(self,item):
        if self.fim < self.tamanho:
            self.itens[self.fim] =item
            self.fim+=1
        else:
            print('lista cheia')

    def inserirDesloc(self,pos,item):
        if self.fim < self.tamanho and abs(pos)<=self.fim:
            #deslocamento
            for i in range(self.fim,pos,-1):
                self.itens[i] = self.itens[i-1]
            self.itens[pos] = item
            self.fim +=1
        else:
            print('lista cheia')

    def remover(self,pos):
        if self.fim > 0 and abs(pos) < self.fim:
            item = self.itens[pos]
            for i in range(pos,self.fim):
                self.itens[i]=self.itens[i+1]
            self.fim -=1
            return item
        else:
            print('lista vazia')

lista = Lista(10)

lista.inserirPos(0,2)
lista.inserirPos(1,3)
lista.inserirPos(2,4)

print(lista.itens)

lista.append(-1)
lista.append(-5)

print(lista.itens)

lista.inserirPos(3, -10)

print(lista.itens)

print(lista.fim)

lista.inserirDesloc(3,-1)

print(lista.itens)

lista.remover(2)

print(lista.itens)

lista.remover(3)

print(lista.itens)