class Node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.head = None
        self.tail = None
        self.current = self.head

    def append(self, item):
        if self.length == 5:
            new_node = Node(item)
            
            # If self.current is None then set it to be the self.head
            if not self.current:
                self.current = self.head

            # Assigning the arrows for the new_node
            new_node.prev = self.current.prev
            new_node.next = self.current.next


            # What if the current node is the self.head? 
            # We need to give the new_node that title
            if self.current is self.head:
                self.head = new_node

            # Re-assigning the arrows towards the new_node
            if self.current.prev:
                self.current.prev.next = new_node
            if self.current.next:
                self.current.next.prev = new_node          
            # Old node should have nothing connected towards it now

            # We need to change self.current to be the next node in line
            if self.current.next:
                self.current = self.current.next
            else: 
                self.current = self.head

        else:
            self.length += 1
            new_node = Node(item)
            if not self.head and not self.tail:
                self.head = new_node
                self.tail = new_node
            else: 
                self.tail.next = new_node
                self.tail = new_node

    def get(self):
        current = self.head
        array = []

        while current is not None:
            array.append(current.value)

            current = current.next

        return array

