from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, item): # adds item to the back of the queue.
    self.storage.add_to_tail(item)
    self.size += 1
  

  def dequeue(self): # Removes and returns an item from the front of the queue.
    if self.size > 0:
      self.size -= 1
    else:
      return None

    return self.storage.remove_from_head()


  def len(self): # returns the number of items in the queue
    return self.size
