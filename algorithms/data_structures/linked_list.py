class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

    def display(self):
        nodes = []
        current = self.head
        cycle_count = 0

        while True:
            nodes.append(current.data)

            if current.next == self.head:
                cycle_count += 1

                if cycle_count == 2:
                    break

            current = current.next

        print(" -> ".join(map(str, nodes)))


if __name__ == "__main__":
    circular_list = CircularLinkedList()

    circular_list.add(1)
    circular_list.add(2)
    circular_list.add(3)

    circular_list.display()
