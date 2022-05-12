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


# def nil():
#     return None


def cons(node: Node, list_):
    if list_ is None:
        list_ = node
    else:
        node.next_ = list_
        list_ = node
    list_.get().next_ = None


# def create():
#     return nil()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    head = None
    cons(Node(('AGH', 'Kraków', 1919)), head)
    cons(Node(('UJ', 'Kraków', 1364)), head)
    cons(Node(('PW', 'Warszawa', 1915)), head)
    temp_node = head


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
