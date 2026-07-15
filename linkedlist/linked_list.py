class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value: int = 1):
        new_node = Node(value=value)

        self.head = new_node
        self.tail = new_node

        self.length = 1

    def print_list(self):

        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value: int) -> bool:
        new_node = Node(value=value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length +=1
            return True
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True

        return False

if __name__ == '__main__':

    linked_list = LinkedList(value=3)
    linked_list.append(value=2)

    linked_list.print_list()