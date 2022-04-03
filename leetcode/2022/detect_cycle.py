class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


def hasCycle(head):

    if not head or not head.next:
        return False

    p1 = head
    p2 = head

    while p2 and p2.next:
        p2 = p2.next.next
        p1 = p1.next

        if p1 == p2:
            return True

    return False


lt = [ListNode(item) for item in [3, 2, 0, -4]]
head = lt[0]
head.next = lt[1]
lt[1].next = lt[2]
lt[2].next = lt[3]
lt[3].next = None

print(hasCycle(head))
