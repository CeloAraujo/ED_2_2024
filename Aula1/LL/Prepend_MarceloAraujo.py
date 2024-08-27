class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        temp = self.head
        pre = self.head
        i = 0
        while temp.next is not None:
            temp = temp.next
            if i == 0:
                i += 1
                continue
            else:
                pre = pre.next

        self.tail=pre 
        pre.next = None
        self.length -= 1
        return temp
    
    def remove(self,value):
         


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('Antes do pop():')
print('----------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Lista encadeada:')
my_linked_list.print_list()


# my_linked_list.prepend(1)
num_retorno = my_linked_list.pop()


print('\n\nDepois do pop():')
print('---------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Lista encadeada:')
my_linked_list.print_list()
print('Numero retornado: ',num_retorno.value)


"""
    EXPECTED OUTPUT:
    
    Antes do pop():
    ----------------
    Head: 1
    Tail: 4
    Length: 4

    Lista encadeada:
    1
    2
    3
    4


    Depois do pop():
    ---------------
    Head: 1
    Tail: 3
    Length: 3 

    Lista encadeada:
    1
    2
    3   

"""
