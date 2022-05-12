# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from copy import deepcopy
import random

# 1 CZĘŚĆ


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

    def __init__(self, tab=None):
        self.size_of_heap = 0
        self.__size = 0
        self.tab = []
        if tab:
            for elem in tab:
                self.enqueue(elem)
            n = int((self.__size // 2) - 1)
            for k in range(n, -1, -1):
                self.heapify(k)

    def heapify(self, index):
        current = index
        previous = index
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

    def is_empty(self):
        if self.__size == 0:
            return True
        return False

    def peek(self):
        return max(self.tab)

    def dequeue(self):
        if self.is_empty():
            return None
        elif self.__size == 1:
            self.__size -= 1
            return self.tab[0]
        else:
            if self.__size > 1:
                root = self.tab[0]
                self.tab[0], self.tab[self.__size-1] = self.tab[self.__size-1], self.tab[0]
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

    def enqueue(self, element):
        if self.is_empty():
            self.tab.append(element)
            self.__size += 1
            self.size_of_heap += 1
        else:
            self.tab.append(element)
            self.__size += 1
            self.size_of_heap += 1
            current = self.__size - 1
            parent_index = self.parent(current)

            while self.tab[current] > self.tab[parent_index]:
                self.tab[parent_index], self.tab[current] = self.tab[current], self.tab[parent_index]
                parent_index = self.parent(self.tab.index(self.tab[parent_index]))

    def print_tab(self):
        print('{', end=' ')
        for i in range(self.size_of_heap - 1):
            print(self.tab[i], end=', ')
        if self.tab[self.size_of_heap - 1]:
            print(self.tab[self.size_of_heap - 1], end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size_of_heap:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


# 2 CZĘŚĆ
def using_swap(tab_):
    priorityQueue_swap = PriorityQueue(tab_)
    for i in range(priorityQueue_swap.size_of_heap):
        min_index = i
        for j in range(i+1, priorityQueue_swap.size_of_heap):
            if priorityQueue_swap.tab[min_index] > priorityQueue_swap.tab[j]:
                min_index = j
        priorityQueue_swap.tab[i], priorityQueue_swap.tab[min_index] = \
            priorityQueue_swap.tab[min_index], priorityQueue_swap.tab[i]
    priorityQueue_swap.print_tab()


def using_shift(tab_):
    priorityQueue_shift = PriorityQueue(tab_)
    for i in range(priorityQueue_shift.size_of_heap):
        min_index = i
        for j in range(i, priorityQueue_shift.size_of_heap):
            if priorityQueue_shift.tab[min_index] > priorityQueue_shift.tab[j]:
                min_index = j
        priorityQueue_shift.tab.insert(i, priorityQueue_shift.tab.pop(min_index))
    priorityQueue_shift.print_tab()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Część 1
    tab_to_send = [Element(elem[1], elem[0]) for elem in
                   [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]]
    priorityQueue = PriorityQueue(tab_to_send)
    priorityQueue.print_tab()
    priorityQueue.print_tree(0, 0)
    while not priorityQueue.is_empty():
        print(priorityQueue.dequeue())
    priorityQueue.print_tab()

    tab_to_send_2 = [random.randint(0, 99) for _ in range(10001)]
    priorityQueue_test_2 = PriorityQueue(tab_to_send_2)
    t_start = time.perf_counter()
    while not priorityQueue_test_2.is_empty():
        print(priorityQueue_test_2.dequeue())
    priorityQueue_test_2.print_tab()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # Część 2
    using_swap(tab_to_send)
    print("Shift")
    using_shift(tab_to_send)

    tab_to_send_3 = [random.randint(0, 1000) for _ in range(10001)]

    t_start_swap = time.perf_counter()
    using_swap(tab_to_send_3)
    t_stop_swap = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop_swap - t_start_swap))

    t_start_shift = time.perf_counter()
    using_shift(tab_to_send_3)
    t_stop_shift = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop_shift - t_start_shift))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
