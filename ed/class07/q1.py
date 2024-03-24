class Celula:
    item = None
    proximo = None
    
    def __init__(self,item):
        self.item = item

class Lista:
    inicio = None
    fim = None
    tamanho = 0
    
    def imprimir(self):
        aux = self.inicio
        while aux != None:
            print(aux.item, end=' ')
            aux = aux.proximo
        print()
    
    def return_list(self):
        aux = self.inicio
        list = []
        while aux != None:
            list.append(aux.item)
            aux = aux.proximo
        return list
        
    def append(self,item):
        c = Celula(item)
        if self.inicio == None:
            self.inicio = c
        else:
            self.fim.proximo = c
        self.fim = c
        self.tamanho += 1
        
    def inserir(self,item,pos):
        if pos >= 0 and pos <= self.tamanho:
            if self.tamanho == 0 or pos == self.tamanho:
                self.append(item)
            else:
                c = Celula(item)
                if pos == 0:
                    c.proximo = self.inicio
                    self.inicio = c
                else:
                    aux = self.inicio
                    cont = 0
                    while cont <pos-1:
                        aux = aux.proximo
                        cont +=1
                    c.proximo = aux.proximo
                    aux.proximo = c
                self.tamanho +=1
        else:
            print('posição inválida!')
            
    def remover(self,pos):
        if pos >0 and pos < self.tamanho:
            if pos == 0:
                c = self.inicio
                self.inicio = self.inicio.proximo
            else:
                aux = self.inicio
                cont = 0
                while cont <pos-1:
                    aux = aux.proximo
                    cont +=1
                c = aux.proximo
                aux.proximo = c.proximo
            item = c.item
            del c
            self.tamanho -=1
            return item
        else:
            print('posição inválida')
    
    def removerItem(self,item):
        if self.tamanho > 0:
            if self.inicio.item == item:
                c = self.inicio
                self.inicio = self.inicio.proximo
                item = c.item
                del c
                self.tamanho -= 1
                return item
            else:
                aux = self.inicio
                while (aux.proximo != None and aux.proximo.item != item ):
                    aux = aux.proximo
                if aux.proximo == None:
                    print('item não encontrado')
                else:
                    c = aux.proximo
                    aux.proximo = c.proximo
                    item = c.item
                    del c
                    self.tamanho -= 1
                    return item
        else:
            print('lista vazia')
            
lista1 = Lista()
lista2 = Lista()

lista1.append(1)
lista1.append(3)
lista1.append(5)
lista1.append(7)

lista2.append(2)
lista2.append(4)
lista2.append(6)
lista2.append(8)

l1 = lista1.return_list()
l2 = lista2.return_list()

print(l1,l2)

def merge(lista1,lista2):
    list_final = []
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            list_final.append(lista1[i])
            list_final.append(lista2[i])
    
    return list_final

print(merge(l1,l2))