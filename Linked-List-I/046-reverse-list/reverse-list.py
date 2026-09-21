# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def reverse_list(head):
#     if not head or not head.next:
#         return head
#     new_head = reverse_list(head.next)
#     head.next.next = head
#     head.next = None
#     return new_head

def reverse_list(head):
    current = head
    previous = None
    while current != None:
        next_node = current.next
        current.next = previous
        previous = current
        current = previous.next
    return previous