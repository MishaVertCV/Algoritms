class LinkedList:
    head = None
    length = 0

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node = None):
            self.element = element
            self.next_node = next_node
    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            self.length += 1
            return element

        node = self.head
        while node.next_node:
            node = node.next_node
            
        node.next_node = self.Node(element)
        self.length += 1
        return element


a = LinkedList()
a.append(4)
a.append(5)
print(a)
