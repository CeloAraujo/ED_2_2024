
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        no_inicial = Node(value)
        self.head = no_inicial
        self.tail = no_inicial
        self.length = 1

    def append(self, value):
        # caso de fronteira
        if self.head == None:
            novo_no = Node(value)
            self.head = novo_no
            self.tail = novo_no
            self.length = 1
        else:
            novo_no = Node(value)  # primeiro passo
            self.tail.next = novo_no  # segundo passo
            self.tail = novo_no  # terceiro passo
            self.length = self.length+1

    # def pop(self,value):

    # def popFirst(self,value):

    # def prepend(self,value):

    # def setValue(self,value):

    # def getValue(self,value):

    # def getValue(self,value):


minha_lista_encadeada = LinkedList(4)
minha_lista_encadeada = LinkedList.append(4, 3)

print('head', minha_lista_encadeada.head.value)
print('tail', minha_lista_encadeada.tail.value)
print('length', minha_lista_encadeada.length)
