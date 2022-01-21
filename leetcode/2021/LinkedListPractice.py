class Node :
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def add_at_beginning(self,new_data):
        #temp = self.head
        new_node = Node(new_data)
        self.head = new_node

    def add_at_pos(self,pos,new_data):
        new_node = Node(new_data)
        temp = self.head
        count = 0
        while(temp):
            if(count==pos):
                new_node.next = temp.next
                temp.next = new_node
                break

            temp= temp.next
            count+=1

    def remove_at_pos(self,pos):
        temp = self.head
        count = 0
        while(temp):
            if(count==pos):
                temp.next=temp.next.next
            temp = temp.next
            count+=1

    def remove_data(self,data):
        temp = self.head
        while(temp):
            if(temp.data==data):
                temp.next=temp.next.next
            temp = temp.next


    def add_last(self, new_data):
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = Node(new_data)

    def print_linkedList(self):
        temp = self.head
        while(temp):
            if(temp.data is not None):
                print(temp.data,end='-->')
            temp = temp.next

    def add_all(self, *argv):
        temp = self.head
        while (temp.next):
            temp = temp.next
        for arg in argv:
            new_node = Node(arg)
            temp.next = new_node
            temp = temp.next


if __name__=='__main__':
    ll = LinkedList()
    ll.add_at_beginning(0)
    ll.add_all(1,2,3,4)
    ll.print_linkedList()
    ll.add_at_pos(2,10)
    print('/n')
    ll.print_linkedList()
    ll.remove_at_pos(1)
    print('/n')
    ll.print_linkedList()
    ll.remove_data(10)
    print('/n')
    ll.print_linkedList()



