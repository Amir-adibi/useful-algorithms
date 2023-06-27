class Node:
    def __init__(self, value):
        self.value = value
        self.next = Node


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.length += 1

    def prepend(self, value):
        self.head.next = self.head
        self.head = Node(value)
        self.length += 1

    def pop(self):
        if self.tail == self.head:
            result = self.tail.value
            self.tail = self.head = 0
            self.length -= 1

            return result

        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next

        result = current_node.value
        self.tail = current_node
        self.length -= 1

        return result

    def insert(self, value, index):
        if index > self.length - 1 or index < 0:
            raise IndexError

        if index == 0:
            self.prepend(value)
            return

        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next

        new_node = Node(value)
        new_node.next = current_node.next
        current_node.next = new_node
        self.length += 1

        return

    def remove(self, index):
        if index > self.length - 1 or index < 0:
            raise IndexError

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        if index == self.length - 1:
            self.pop()
            return

        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next

        target_node = current_node.next
        current_node.next = target_node.next
        self.length -= 1

        return

    def get(self, index):
        if index > self.length - 1 or index < 0:
            raise IndexError

        current_node = self.head
        for i in range(index):
            current_node = current_node.next

        return current_node.value


my_LL = LinkedList(1)
my_LL.append(3)
my_LL.append(5)
my_LL.append(7)

print('(', end='')
for i in range(my_LL.length):
    if i == my_LL.length - 1:
        print(my_LL.get(i), end='')
    else:
        print(my_LL.get(i), end=', ')

print(')')

print('head is:', my_LL.head.value)
print('tail is:', my_LL.tail.value)

print('------------')

my_LL.insert(2, 1)
my_LL.insert(4, 3)
my_LL.insert(6, 5)

print('(', end='')
for i in range(my_LL.length):
    if i == my_LL.length - 1:
        print(my_LL.get(i), end='')
    else:
        print(my_LL.get(i), end=', ')

print(')')

print('head is:', my_LL.head.value)
print('tail is:', my_LL.tail.value)

print('------------')

my_LL.pop()

print('(', end='')
for i in range(my_LL.length):
    if i == my_LL.length - 1:
        print(my_LL.get(i), end='')
    else:
        print(my_LL.get(i), end=', ')

print(')')

print('head is:', my_LL.head.value)
print('tail is:', my_LL.tail.value)

print('------------')

my_LL.remove(0)
my_LL.remove(0)
my_LL.remove(1)

print('(', end='')
for i in range(my_LL.length):
    if i == my_LL.length - 1:
        print(my_LL.get(i), end='')
    else:
        print(my_LL.get(i), end=', ')

print(')')

print('head is:', my_LL.head.value)
print('tail is:', my_LL.tail.value)

print('------------')

my_LL.remove(2)

print('(', end='')
for i in range(my_LL.length):
    if i == my_LL.length - 1:
        print(my_LL.get(i), end='')
    else:
        print(my_LL.get(i), end=', ')

print(')')

print('head is:', my_LL.head.value)
print('tail is:', my_LL.tail.value)

print('------------')
