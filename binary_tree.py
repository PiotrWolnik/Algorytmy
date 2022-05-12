from operator import attrgetter
from collections import deque


class Node:
    def __init__(self, key, value, left_child=None, right_child=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def get(self):
        return self.key, self.value


class BinaryTree:
    def __init__(self):
        self.head = None
        self.__nodes = []

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def search(self, key, node=None):
        if node is None:
            node = self.head
        while node is not None:
            if key > node.key:
                node = node.right_child
            elif key < node.key:
                node = node.left_child
            else:
                return node.value
        return None

    def insert(self, key, data):
        if self.isEmpty():
            node_to_add = Node(key, data)
            self.head = node_to_add
            self.__nodes.append(node_to_add)
        else:
            temp_val = self.search(key)
            if temp_val is None:
                iterator = self.head
                previous = self.head
                while True:
                    previous = iterator
                    if iterator.key > key:
                        iterator = iterator.left_child
                        if iterator is None:
                            break
                        else:
                            continue
                    else:
                        iterator = iterator.right_child
                        if iterator is None:
                            break
                        else:
                            continue
                node_to_add = Node(key, data)
                if previous.key > key:
                    previous.left_child = node_to_add
                else:
                    previous.right_child = node_to_add
                self.__nodes.append(node_to_add)
            else:
                current_node = self.head
                while current_node.key is not key:
                    if current_node.key > key:
                        current_node = current_node.left_child
                    else:
                        current_node = current_node.right_child
                current_node.value = data

    def delete(self, key):
        if self.isEmpty():
            raise Exception("Binary tree is already empty!")
        keys = [node.key for node in self.__nodes]
        if key not in keys:
            raise Exception("Such key does not exist!")
        else:
            # We delete node with key given as an argument from private attribute
            for n in self.__nodes:
                if n.key == key:
                    self.__nodes.remove(n)
                    break

            temp = self.head
            previous = self.head
            while temp.key != key:
                previous = temp
                if key > temp.key:
                    temp = temp.right_child
                    continue
                else:
                    temp = temp.left_child
                    continue
            # We found the node with such key in our binary tree
            # We have 3 cases:

            # Case1 without child nodes
            if temp.left_child is None and temp.right_child is None:
                if previous.key < temp.key:
                    previous.right_child = None
                else:
                    previous.left_child = None

            # Case2 with one child
            # We check if temp node has a left child if not than it means it has right child
            elif temp.left_child is not None and temp.right_child is None:
                if temp.key < previous.key:
                    previous.left_child = temp.left_child
                else:
                    previous.right_child = temp.left_child
            elif temp.left_child is None and temp.right_child is not None:
                if temp.key < previous.key:
                    previous.left_child = temp.right_child
                else:
                    previous.right_child = temp.right_child

            # Case3 with two children. Here we have 2 situations:
            # (1) The right subtree has a left child in the end
            # (2) There is no left child in the end so we will have to
            #     delete the node before the right child
            else:
                right_subtree_temp = temp.right_child
                # The node that will store min key
                min_key = right_subtree_temp
                previous_for_min_key = temp
                while True:
                    if right_subtree_temp.right_child is None and right_subtree_temp.left_child is not None:
                        if min_key.key > right_subtree_temp.left_child.key:
                            previous_for_min_key = right_subtree_temp
                            min_key = right_subtree_temp.left_child
                        right_subtree_temp = right_subtree_temp.left_child
                        continue
                    elif right_subtree_temp.left_child is None and right_subtree_temp.right_child is not None:
                        right_subtree_temp = right_subtree_temp.right_child
                        continue
                    elif right_subtree_temp.left_child is not None and right_subtree_temp.right_child is not None:
                        if min_key.key > right_subtree_temp.left_child.key:
                            previous_for_min_key = right_subtree_temp
                            min_key = right_subtree_temp.left_child
                        right_subtree_temp = right_subtree_temp.left_child
                        continue
                    else:
                        break
                # Situation (1)
                if min_key.left_child is None and min_key.right_child is None:
                    if temp == self.head:
                        previous_for_min_key.left_child = None
                        right_sub = temp.right_child
                        left_sub = temp.left_child
                        self.head = Node(min_key.key, min_key.value)
                        self.head.right_child = right_sub
                        self.head.left_child = left_sub
                    else:
                        # We delete min_key from binary_tree
                        if previous_for_min_key.key == temp.key:
                            left_sub = temp.left_child
                            if previous.key > temp.key:
                                previous.left_child = Node(min_key.key, min_key.value)
                                previous.left_child.left_child = left_sub
                            else:
                                previous.right_child = Node(min_key.key, min_key.value)
                                previous.right_child.left_child = left_sub
                        else:
                            previous_for_min_key.left_child = None
                            right_sub = temp.right_child
                            left_sub = temp.left_child
                            if previous.key > temp.key:
                                previous.left_child = Node(min_key.key, min_key.value)
                                previous.left_child.left_child = left_sub
                                previous.left_child.right_child = right_sub
                            else:
                                previous.right_child = Node(min_key.key, min_key.value)
                                previous.right_child.left_child = left_sub
                                previous.right_child.right_child = right_sub

                # Situation (2)
                else:
                    if temp == self.head:
                        previous_for_min_key.left_child = None
                        right_sub = min_key.right_child
                        left_sub = temp.left_child
                        self.head = Node(min_key.key, min_key.value)
                        self.head.right_child = right_sub
                        self.head.left_child = left_sub
                    else:
                        right_sub_of_key = min_key.right_child
                        left_sub = temp.left_child
                        if min_key.right_child is not None:
                            if previous_for_min_key.left_child.key == min_key.key:
                                previous_for_min_key.left_child = min_key.right_child
                            else:
                                previous_for_min_key.right_child = min_key.right_child
                        else:
                            if previous_for_min_key.left_child.key == min_key.key:
                                previous_for_min_key.left_child = None
                            else:
                                previous_for_min_key.right_child = None
                        if previous.key > temp.key:
                            previous.left_child = Node(min_key.key, min_key.value)
                            previous.left_child.right_child = right_sub_of_key
                            previous.left_child.left_child = left_sub
                        else:
                            previous.right_child = Node(min_key.key, min_key.value)
                            previous.right_child.right_child = right_sub_of_key
                            previous.right_child.left_child = left_sub

    def print_tree(self):
        print("==============")
        self._print_tree(self.head, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right_child, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self._print_tree(node.left_child, lvl + 5)

    def height(self, node=None):
        if node is None:
            node = self.head
        if node is None:
            return 0
        height_of_binary_tree = 0
        queue = deque()
        queue.append(node)
        while queue:
            size_of_queue = len(queue)
            while size_of_queue > 0:
                front = queue.popleft()
                if front.left_child:
                    queue.append(front.left_child)
                if front.right_child:
                    queue.append(front.right_child)
                size_of_queue = size_of_queue - 1
            height_of_binary_tree = height_of_binary_tree + 1

        return height_of_binary_tree

    def print(self):
        if self.isEmpty():
            print("[]")
        else:
            self.__nodes.sort(key=attrgetter('key'))
            elems = len(self.__nodes)
            i = 0
            string = "["
            for node in self.__nodes:
                if i == elems - 1:
                    string += f"{node.key}:{node.value}]"
                else:
                    string += f"{node.key}:{node.value}, "
                i += 1
            print(string)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    binary_tree = BinaryTree()
    binary_tree.insert(50, 'A')
    binary_tree.insert(15, 'B')
    binary_tree.insert(62, 'C')
    binary_tree.insert(5, 'D')
    binary_tree.insert(20, 'E')
    binary_tree.insert(58, 'F')
    binary_tree.insert(91, 'G')
    binary_tree.insert(3, 'H')
    binary_tree.insert(8, 'I')
    binary_tree.insert(37, 'J')
    binary_tree.insert(60, 'K')
    binary_tree.insert(24, 'L')
    binary_tree.print_tree()
    binary_tree.print()
    print(binary_tree.search(24))
    binary_tree.insert(20, "AA")
    binary_tree.insert(6, 'M')
    binary_tree.delete(62)
    binary_tree.insert(59, 'N')
    binary_tree.insert(100, 'P')
    binary_tree.delete(8)
    binary_tree.delete(15)
    binary_tree.insert(55, 'R')
    binary_tree.delete(50)
    binary_tree.delete(5)
    binary_tree.delete(24)
    print(binary_tree.height())
    binary_tree.print()
    binary_tree.print_tree()

