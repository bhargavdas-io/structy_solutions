class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
  current = head
  list = []
  while current != None:
    list.append(current.val)
    current = current.next
  print(list)
    

