class Node:
    def __init__(self, key, v):
        self.key = key
        self.v = v
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def is_empty(self):
        return self.head.next == self.tail

    def pop_left(self):
        node = self.head.next
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.freq_to_list = {}
        self.c = capacity
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node, f = self.key_to_node[key]

            self.freq_to_list[f].remove(node)

            if f == self.min_freq and self.freq_to_list[f].is_empty():
                self.min_freq += 1

            if f + 1 not in self.freq_to_list:
                self.freq_to_list[f + 1] = DoublyLinkedList()

            self.freq_to_list[f + 1].append(node)
            self.key_to_node[key] = (node, f + 1)

            return node.v

        return -1

    def put(self, key: int, value: int) -> None:
        if self.c == 0:
            return

        if key in self.key_to_node:
            node, f = self.key_to_node[key]
            node.v = value
            self.get(key)
            return

        if len(self.key_to_node) == self.c:
            node = self.freq_to_list[self.min_freq].pop_left()
            del self.key_to_node[node.key]

        node = Node(key, value)

        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()

        self.freq_to_list[1].append(node)
        self.key_to_node[key] = (node, 1)
        self.min_freq = 1