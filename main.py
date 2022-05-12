# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Node:
    def __init__(self, size=6):
        self.tab = [None for _ in range(size)]
        self.size = size
        self.next = None
        self.contents = 0

    def __str__(self):
        return str(self.tab)


class UnrolledLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def get(self, index):
        amount_of_elements = (self.length() * self.head.size) - 1
        if index > amount_of_elements:
            raise Exception("Trying to reach element out of scope!")
        else:
            if index <= self.head.size - 1:
                return self.head.tab[index]
            else:
                node_which_stores_index = (index // (self.head.size-1)) + 1 \
                                            if index % (self.head.size-1) != 0 else (index // (self.head.size-1))
                temp = self.head
                i = 1
                # print(node_which_stores_index)
                while i < node_which_stores_index:
                    i += 1
                    temp = temp.next
                index %= temp.size - 1
                return temp.tab[index]

    def length(self):
        if self.is_empty():
            return 0
        temp = self.head
        i = 0
        while temp is not None:
            i += 1
            temp = temp.next
        return i

    def insert(self, index, data):
        if self.is_empty():
            self.head = Node()
            if index > self.head.size - 1:
                self.head.tab[-1] = data
            else:
                self.head.tab[index] = data
            self.head.contents += 1
        else:
            temp = self.head
            if temp.contents == temp.size:
                new_node = Node(temp.size)
                new_node.tab[:(temp.contents // 2):] = [i for i in temp.tab[(temp.contents // 2):temp.contents]]
                if temp.next is not None:
                    next_node = temp.next
                    next_node.next = None
                    new_node.next = next_node
                temp.next = new_node
                # print(temp.size)
                temp.tab[(temp.contents // 2):temp.size] = [None for _ in range(temp.size - (temp.contents//2))]
                temp.contents -= len(temp.tab[(temp.contents // 2):temp.contents])
                if index > temp.size-1:
                    node_which_stores_index = (index // (self.head.size-1)) + 1 \
                                            if index % (self.head.size-1) != 0 else (index // (self.head.size-1))

                    node_to_insert = self.head
                    i = 1
                    while i < node_which_stores_index:
                        i += 1
                        node_to_insert = node_to_insert.next
                    index %= self.head.size-1
                    # print(index)
                    node_to_insert.tab.insert(index-1, data)
                    node_to_insert.tab.pop(-1)
                    node_to_insert.contents += 1
                else:
                    temp.tab.insert(index, data)
                    temp.tab.pop(-1)
                    temp.contents += 1
            else:
                if index > temp.size-1:
                    node_which_stores_index = (index // (self.head.size-1)) + 1 \
                                            if index % (self.head.size-1) != 0 else (index // (self.head.size-1))

                    node_to_insert = self.head
                    i = 1
                    while i < node_which_stores_index:
                        i += 1
                        node_to_insert = node_to_insert.next
                    index %= self.head.size-1
                    # print(index)
                    node_to_insert.tab.insert(index-1, data)
                    node_to_insert.tab.pop(-1)
                    node_to_insert.contents += 1
                else:
                    temp.tab.insert(index, data)
                    temp.tab.pop(-1)
                    temp.contents += 1

    def delete(self, index):
        if self.is_empty():
            raise Exception("Trying to delete element from list that is empty.")
        elif index > self.length() * self.head.size - 1:
            raise Exception("Trying to delete index that does not exist")
        if index < self.head.size - 1:
            if self.head.contents < self.head.size / 2:
                if self.head.next is None:
                    self.head.tab.pop(index)
                    self.head.contents -= 1
                else:
                    temp = self.head
                    temp = temp.next
                    self.head.insert(index, temp.tab[0])
                    temp.tab[0] = None

                    temp.contents -= 1
                    if temp.contents < temp.size / 2:
                        for i in range(temp.size-1):
                            if temp.tab[i] is None:
                                continue
                            else:
                                self.head.insert(index, temp.tab[i])
                                self.head.tab.pop(-1)
                                temp.tab[i] = None
                                temp.contents -= 1
                        self.head.next = None
            else:
                self.head.tab.pop(index)
                self.head.contents -= 1
                self.head.tab.insert(-1, None)
        else:
            node_index_to_delete = (index // (self.head.size-1)) + 1 \
                                            if index % (self.head.size-1) != 0 else (index // (self.head.size-1))
            i = 0
            node_from_which_we_delete = self.head
            while i < node_index_to_delete:
                i += 1
                node_from_which_we_delete = node_from_which_we_delete.next
            index %= self.head.size-1
            if node_from_which_we_delete.contents < node_from_which_we_delete.size / 2:
                if node_from_which_we_delete.next is None:
                    node_from_which_we_delete.tab.pop(index)
                    node_from_which_we_delete.contents -= 1
                else:
                    temp = node_from_which_we_delete
                    temp = temp.next
                    node_from_which_we_delete.insert(index, temp.tab[0])
                    temp.tab[0] = None
                    temp.contents -= 1
                    if temp.contents < temp.size / 2:
                        for i in range(temp.size - 1):
                            if temp.tab[i] is None:
                                continue
                            else:
                                node_from_which_we_delete.insert(index, temp.tab[i])
                                node_from_which_we_delete.tab.pop(-1)
                                temp.tab[i] = None
                                temp.contents -= 1
                        node_from_which_we_delete.next = temp.next
            else:
                node_from_which_we_delete.tab.pop(index)
                node_from_which_we_delete.contents -= 1
                node_from_which_we_delete.tab.insert(-1, None)

    def print_unrolled_list(self):
        if self.is_empty():
            print("[]")
        temp = self.head
        string = ""
        while temp is not None:
            if temp.next is None:
                string += temp.__str__()
            else:
                string += temp.__str__() + " -> "
            temp = temp.next
        print(string)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ull = UnrolledLinkedList()
    for j in range(1, 10):
        ull.insert(0, j)
    print(ull.get(4))
    ull.insert(1, 10)
    ull.insert(8, 11)
    ull.print_unrolled_list()
    ull.delete(1)
    ull.print_unrolled_list()
    ull.delete(2)
    ull.print_unrolled_list()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
