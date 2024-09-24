class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
    
class listaEncadeadaDupla:
    def __init__(self,value):
        no_inicial = Node(value)
        self.head = no_inicial
        self.tail = no_inicial
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        temp = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp




if __name__ == '__main__':
    dll = listaEncadeadaDupla(12456786)
    print('Tail antes: ', dll.tail.value)
    dll.append(15)
    print('Tail depois: ', dll.tail.value)
