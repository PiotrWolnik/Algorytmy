# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Queue:

    def __init__(self, size=5):
        self.size = size
        self.tab = [None for i in range(size)]
        self.save_to_queue = 0
        self.read_from_queue = 0

    def is_empty(self):
        if self.read_from_queue == self.save_to_queue:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[self.read_from_queue]

    def dequeue(self):
        if self.is_empty():
            return None
        if self.read_from_queue == self.size-1:
            data_to_return = self.tab[self.read_from_queue]
            self.tab[self.read_from_queue] = None
            self.read_from_queue = 0
        else:
            data_to_return = self.tab[self.read_from_queue]
            self.tab[self.read_from_queue] = None
            self.read_from_queue += 1
        return data_to_return

    def enqueue(self, data):
        if self.is_empty():
            self.tab[self.save_to_queue] = data
            self.save_to_queue += 1
        else:
            if self.save_to_queue != self.read_from_queue:
                self.tab[self.save_to_queue] = data
                self.save_to_queue += 1
                if self.save_to_queue == self.size:
                    self.tab = self.realloc(self.size * 2)
                    self.save_to_queue = 0
                    self.read_from_queue = self.size + self.read_from_queue
                    self.size = len(self.tab)
            else:
                self.tab = self.realloc(self.size*2)
                self.save_to_queue = 0
                self.read_from_queue = self.size + self.read_from_queue
                self.size = len(self.tab)

    def realloc(self, size):
        """Wprowadziłem drobną modyfikację w funkcji realloc"""
        oldSize = len(self.tab)
        difference_between_sizes = size - oldSize
        for i in range(difference_between_sizes):
            self.tab.insert(i, None)
        return self.tab

    def print_tab(self):
        print(self.tab)

    def print_queue(self):
        if self.is_empty():
            print("[]")
        else:
            string = "["
            read_index = self.read_from_queue
            while self.tab[self.read_from_queue] is not None:
                if self.read_from_queue == self.size - 1:
                    if self.tab[self.read_from_queue] is None:
                        string += "]"
                    else:
                        string += f"{self.tab[self.read_from_queue]}, "
                    self.read_from_queue = 0
                else:
                    if self.tab[self.read_from_queue + 1] is None:
                        string += f"{self.tab[self.read_from_queue]}]"
                    else:
                        string += f"{self.tab[self.read_from_queue]}, "
                    self.read_from_queue += 1
            self.read_from_queue = read_index
            print(string)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.dequeue())
    print(queue.peek())

    queue.print_queue()

    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.print_tab()
    queue.print_queue()

    while not queue.is_empty():
        print(queue.dequeue())

    queue.print_queue()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
