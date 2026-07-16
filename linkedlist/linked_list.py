
class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        

class LinkedList:
    
    def __init__(self, value: int):
        new_node = Node(value=value)
        
        self.head = new_node
        self.tail = new_node
        
        self.length = 1 
        
    def _new_node(self, value: int):
        new_node = Node(value=value)
        
        self.head = new_node
        self.tail = new_node
        self.length += 1
        
    def print_list(self):
        temp = self.head 
        
        while temp:
            print(temp.value)
            temp = temp.next
            
    def append(self, value: int):
        
        if not self.head or self.length == 0:
            self._new_node(value=value)
            return True
        
        new_node = Node(value=value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True
        
    def prepend(self, value: int):
        
        if not self.head or self.length == 0:
            self._new_node(value=value)
            return True
        
        new_node = Node(value=value)
        
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if not self.head or self.length == 0:
            return None
            
        self.head = self.head.next
        self.length -= 1
    
    def pop(self):
        if not self.head or self.length == 0:
            return None
            
        temp = self.head
        pre = self.head
        
        while temp.next:
            pre = temp
            temp = temp.next
            
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return temp
    
    def get(self, index: int):
        if index < 0 or index >= self.length:
            return None
            
        temp = self.head    
        count = 0
        
        while index > count:
            temp = temp.next
            count += 1

        return temp.value
    
    def set(self, index: int, value: int):
        if index < 0 or index >= self.length:
            return None
            
        temp = self.head    
        count = 0
        
        while index > count:
            temp = temp.next
            count += 1

        temp.value = value

        return temp.value
    
    def remove(self, index: int):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            self.pop_first()
            return None

        if index == self.length - 1:
            self.pop()
            return None
            
        temp = self.head   
        pre = self.head 
        count = 0
        
        while index > count:
            pre = temp
            temp = temp.next
            count += 1

        pre.next = temp.next
        temp.next = None
        self.length -= 1

        return temp
    
if __name__ == "__main__":
    
    linked_list = LinkedList(value=4)
    linked_list.append(value=3)
    linked_list.append(value=2)
    linked_list.append(value=1)
    
    linked_list.prepend(value=5)
    
    # linked_list.pop_first()
    # linked_list.pop()
    
    # print("The GET return -->", linked_list.get(index=1))

    linked_list.set(index=3, value= 55)

    linked_list.remove(index=2)
    
    linked_list.print_list()