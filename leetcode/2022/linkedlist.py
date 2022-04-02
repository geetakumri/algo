# Creating node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # add node into beginning of linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        return new_node

    # Function to remove all occurrences
    # of duplicate elements
    def removeAllDuplicates(self, temp):

        # temp is head node of linkedlist
        curr = temp
        # print(' print something')
        head = prev = Node(None)
        head.next = curr

        # Here we use same as we do in removing
        # duplicates and only extra thing is that
        # we need to remove all elements
        # having duplicates that we did in 30-31
        while curr and curr.next:

            # until the current value and next
            # value are same keep updating the current value
            if curr.val == curr.next.val:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next

                    # still one of duplicate values left
                    # so point prec to curr
                curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        return head.next

    # for print the linkedlist
    def printList(self):
        temp1 = self.head
        while temp1 is not None:
            print(temp1.val, end=" ")
            temp1 = temp1.next

    # For getting head of linkedlist
    def get_head(self):
        return self.head


# Driver Code
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(53)
    llist.push(53)
    llist.push(49)
    llist.push(49)
    llist.push(35)
    llist.push(28)
    llist.push(28)
    llist.push(23)

    print("Created linked list is:")
    llist.printList()
    print("\nLinked list after deletion of duplicates:")
    head1 = llist.get_head()
    # print(head1)
    llist.removeAllDuplicates(head1)
    llist.printList()
