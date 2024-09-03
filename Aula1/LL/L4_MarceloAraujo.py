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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

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

    ## ESCREVA O MÉTODO REMOVE() ##
    def remove(self, value):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        temp = self.head
        if temp.value == value:  # verificação se valor é o head
            pos = temp.next
            self.head = pos
            temp.next = None
            self.length -= 1
            return True
        elif self.tail == value:  # verificação se valor é o tail
            pre = self.head
            i = 0
            while temp.next is not None:
                temp = temp.next
                if i == 0:
                    i += 1
                    continue
                else:
                    pre = pre.next
            self.tail = pre
            pre.next = None
            self.length -= 1
            return True
        else:
            pre = self.head
            i = 0
            while temp.value != value:
                temp = temp.next
                if i == 0:
                    i += 1
                    continue
                else:
                    pre = pre.next
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            self.tail = pre
            return True

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            primeiro = self.head
            self.head = None
            self.tail = None
        else:
            primeiro = self.head
            segundo = self.head.next
            self.head = segundo
        self.length -= 1
        return primeiro

    def get(self, index):
        if index < 0 or index > (self.length-1):
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set(self, index, value):
        if index < 0 or index > (self.length-1):
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return True

    def remove_idx(self, index):
        if index < 0 or index > (self.length-1):
            return False
        if index == 0:
            return self.pop_first()
        if index == (self.length-1):
            return self.pop()

        ant = self.get(index-1)
        temp = ant.next

        removido = temp
        temp = temp.next

        ant.next = temp
        self.length -= 1
        return removido


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print('LL antes do remove():')
my_linked_list.print_list()

print('\nNo removido:')
print(my_linked_list.remove(2).value)
print('LL depois do remove() no meio da lista:')
my_linked_list.print_list()

print('\nNo removido:')
print(my_linked_list.remove(0).value)
print('LL depois do remove() do primeiro no:')
my_linked_list.print_list()

print('\nNo removido:')
print(my_linked_list.remove(2).value)
print('LL depois do remove() do ultimo no:')
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    LL antes do remove():
    1
    2
    3
    4
    5

    No removido:
    3
    LL depois do remove() no meio da lista:
    1
    2
    4
    5

    No removido:
    1
    LL depois do remove() do primeiro no:
    2
    4
    5

    No removido:
    5
    LL depois do remove() do ultimo no:
    2
    4

"""
