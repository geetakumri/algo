class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()

    def printList(self):
        temp = self.head
        while (temp):
            if (temp.data is not None):
                print(temp.data, end=" --> ")
            temp = temp.next

    def add_first(self, new_data):
        new_node = Node(new_data)
        # new_node.next = self.head
        self.head = new_node

    def add_last(self, new_data):
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = Node(new_data)

    def add_all(self, *argv):
        temp = self.head
        while (temp.next):
            temp = temp.next
        for arg in argv:
            new_node = Node(arg)
            temp.next = new_node
            temp = temp.next

    def add_middle(self, num, new_data):
        temp = self.head
        new_node = Node(new_data)
        while (temp):
            if (temp.data == num):
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next

    def delete_first(self):
        temp = self.head
        

if __name__ == '__main__':
    ll = LinkedList()
    # ll.add_all("geeta","saurav","puchu")

    # ll.printList()
    ll.add_first(4)
    ll.add_last(3)
    ll.add_last(5)
    ll.add_middle(3, 6)

    ll.add_all("geeta", "saurav", "puchu")
    ll.printList()

    ll.delete_first()
