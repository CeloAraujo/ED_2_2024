class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            self.head = Node(value)
            self.tail = self.head
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


def merge_sorted_linked_lists(ll1, ll2):
    dummy = Node(0)  
    current = dummy 
    

    p1 = ll1.head
    p2 = ll2.head

    while p1 and p2:
        if p1.value <= p2.value:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    

    if p1:
        current.next = p1
    

    if p2:
        current.next = p2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    
    return merged_list





# Cria a primeira lista encadeada
ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(4)

# Cria a segunda lista encadeada
ll2 = LinkedList()
ll2.append(1)
ll2.append(3)
ll2.append(4)

# Mescla as duas listas
ll3 = merge_sorted_linked_lists(ll1, ll2)

# Imprime as listas
print("Lista 1:")
ll1.print_list()
print("Lista 2:")
ll2.print_list()
print("Lista Mesclada:")
ll3.print_list()
