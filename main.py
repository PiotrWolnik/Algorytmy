#skończone
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Element:

    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"{self.priority} : {self.data}"


# Priority Queue
class PriorityQueue:

    def __init__(self):
        self.tab = []
        self.__size = 0

    def is_empty(self):
        if self.__size == 0:
            return True
        return False

    def peek(self):
        return max(self.tab)

    def dequeue(self):
        # def recursive(i):
        #     current_ = i
        #     left_child_ = self.left(i)
        #     right_child_ = self.right(i)
        #     if left_child_ <= self.__size - 1 and self.tab[left_child_] > self.tab[current_]:
        #         current_ = left_child_
        #     if right_child_ <= self.__size and self.tab[right_child_] > self.tab[current_]:
        #         current_ = right_child_
        #     if i != current_:
        #         self.tab[i], self.tab[current_] = self.tab[current_], self.tab[i]
        #         recursive(current_)
        # to_delete = self.tab[0]
        # self.tab[0] = self.tab[self.__size-1]
        # self.__size -= 1
        # recursive(0)
        # current = 0
        #
        # return to_delete
        if self.is_empty():
            return None
        elif self.__size == 1:
            self.__size -= 1
            return self.tab.pop().data
        else:
            if self.__size > 1:
                root = self.tab[0].data
                last_element = self.tab.pop()
                self.tab[0] = last_element
                self.__size -= 1
                current = 0
                previous = 0
                while True:
                    right_child = self.right(current)
                    left_child = self.left(current)
                    if left_child < self.__size - 1 and self.tab[left_child] > self.tab[current]:
                        current = left_child
                    if right_child < self.__size - 1 and self.tab[right_child] > self.tab[current]:
                        current = right_child
                    if current != previous:
                        self.tab[previous], self.tab[current] = self.tab[current], self.tab[previous]
                        previous = current
                    else:
                        break
                return root

    def left(self, index):
        return 2 * (index + 1) - 1

    def right(self, index):
        return 2 * (index + 1)

    def parent(self, index):
        return (index - 1) // 2

    def enqueue(self, data, priority):
        element_to_add = Element(data, priority)
        if self.is_empty():
            self.tab.append(element_to_add)
            self.__size += 1
        else:
            self.__size += 1
            self.tab.append(Element(data, priority))
            current = self.__size-1
            parent_index = self.parent(current)

            while self.tab[current] > self.tab[parent_index]:
                self.tab[parent_index], self.tab[current] = self.tab[current], self.tab[parent_index]
                parent_index = self.parent(self.tab.index(self.tab[parent_index]))

    def print_tab(self):
        if self.is_empty():
            print("{}")
        else:
            print('{', end=' ')
            for i in range(self.__size - 1):
                print(self.tab[i], end=', ')
            if self.tab[self.__size - 1]:
                print(self.tab[self.__size - 1], end=' ')
            print('}')

    def print_tree(self, idx, lvl):
        if idx < self.__size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    priorityQueue = PriorityQueue()

    for key_, value_ in zip([4, 7, 6, 7, 5, 2, 2, 1], "ALGORYTM"):
        priorityQueue.enqueue(value_, key_)

    priorityQueue.print_tree(0, 0)
    priorityQueue.print_tab()
    print(priorityQueue.dequeue())
    print(priorityQueue.peek())
    priorityQueue.print_tab()
    while not priorityQueue.is_empty():
        print(priorityQueue.dequeue())
    priorityQueue.print_tab()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
