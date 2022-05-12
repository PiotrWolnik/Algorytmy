# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Node:
    def __init__(self, data):
        self.data_ = data
        self.next_ = None

    def get(self):
        return self

    def __str__(self):
        return f"{self.data_}"


class LinkedList:

    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self) -> int:
        if self.head is None:
            return 0
        else:
            node_ = self.head
            i = 0
            while node_ is not None:
                i += 1
                node_ = node_.next_
            return i

    def get(self):
        return self.head.get().data_

    def add(self, new_node):
        if self.length() == 0:
            self.head = new_node
        else:
            prev_head = self.head
            new_node.next_ = self.head
            self.head = new_node
            prev_head.get().next_ = None

    def remove(self):
        if self.length() == 0:
            raise Exception("Your list is already empty!")
        elif self.length() == 1:
            self.destroy()
        else:
            node_to_remove = self.head
            self.head = node_to_remove.next_
            node_to_remove = None

    def add_at_end(self, new_node):
        if self.length() == 0:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next_ is not None:
                temp_node = temp_node.next_
            temp_node.next_ = new_node
        new_node.next_ = None

    def remove_at_end(self):
        if self.length() == 0:
            raise Exception("Your list is already empty!")
        elif self.length() == 1:
            self.destroy()
        else:
            temp_node = self.head
            prev_node = self.head
            while temp_node.next_ is not None:
                prev_node = temp_node
                temp_node = temp_node.next_
            temp_node = None
            prev_node.next_ = None

    def __str__(self):
        if self.length() > 0:
            string = "["
            temp_node = self.head
            while temp_node is not None:
                if temp_node.next_ is None:
                    string += temp_node.__str__() + "]\n"
                else:
                    string += temp_node.__str__() + ",\n"
                temp_node = temp_node.next_
            return string
        else:
            return "Your list is empty."

    def take(self, n: int):
        new_linked_list = LinkedList()
        if n > self.length():
            node_ = self.head
            while node_ is not None:
                new_linked_list.add_at_end(Node(node_.get()))
                node_ = node_.next_
        else:
            i = 0
            node_ = self.head
            while i < n:
                new_linked_list.add_at_end(Node(node_.get()))
                i += 1
                node_ = node_.next_

        return new_linked_list

    def drop(self, n: int):
        new_linked_list = LinkedList()
        if n < self.length():
            node_ = self.head
            i = 0
            while i < n:
                i += 1
                node_ = node_.next_
            while node_ is not None:
                new_linked_list.add_at_end(Node(node_.get()))
                node_ = node_.next_
        return new_linked_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add(Node(('UJ', 'Kraków', 1364)))
    linked_list.add(Node(('AGH', 'Kraków', 1919)))
    linked_list.add_at_end(Node(('PW', 'Warszawa', 1915)))
    linked_list.add_at_end(Node(('UW', 'Warszawa', 1915)))
    print(f"\nCurrent size of the list = {linked_list.length()}.\n\nHere's the data stored in your list:")
    print(linked_list.__str__())

    print(f"\nLet's see what's being stored as the frist element of the list:\n{linked_list.get()}\n")

    print("\nHere's the data after remove-at-the-beginning-of-the-list operation:")
    linked_list.remove()
    print(linked_list.__str__())

    print("\nHere's the data after remove-at-the-end-of-the-list operation:")
    linked_list.remove_at_end()
    print(linked_list.__str__())

    print("\nNow we will use destroy-the-list operation:")
    linked_list.destroy()
    if linked_list.is_empty():
        print("List is empty.")

    list_of_nodes_to_add = [('AGH', 'Kraków', 1919),
                            ('UJ', 'Kraków', 1364),
                            ('PW', 'Warszawa', 1915),
                            ('UW', 'Warszawa', 1915),
                            ('UP', 'Poznań', 1919),
                            ('PG', 'Gdańsk', 1945)]
    for node in list_of_nodes_to_add:
        linked_list.add_at_end(Node(node))

    print("\nLet's see the linked list with all nodes we need:")
    print(linked_list)

    print("\nNow we create new_linked_list from elements that already exist in our linked_list via take(n) function.")
    print("First three elements:")
    new_linked_list_ = linked_list.take(3)  # In this case we use just first three
    print(new_linked_list_)
    new_linked_list_.destroy()
    print("All elements:")
    new_linked_list_ = linked_list.take(10)  # In this case we check if all elements are copied when n is bigger than
    print(new_linked_list_)                  # size of list

    print("\nNow we create new_linked_list from elements that already exist in our linked_list via drop(n) function.")
    print("All elements without the first three:")
    new_linked_list2_ = linked_list.drop(3)  # We take all the elements except the first three
    print(new_linked_list2_)
    new_linked_list2_.destroy()
    print("No elements:")
    new_linked_list2_ = linked_list.drop(10)  # We check if drop(n) function returns empty list when n is bigger
    if new_linked_list2_.is_empty():          # than size of list
        print("List is empty.")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
