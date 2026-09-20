# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_nodes(head):
    if not head or not head.next:
        return head
    new_head = reverse_nodes(head.next)
    head.next.next = head
    head.next = None
    return new_head