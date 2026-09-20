# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
    curr = head
    index_track = 0
    while curr != None:
        if index != index_track:
            curr = curr.next
            index_track += 1
        return curr.val
  
