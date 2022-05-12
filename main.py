# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key} : {self.value}"


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def hash(self, key):
        if isinstance(key, str):
            key_int = 0
            for letter in key:
                key_int += ord(letter)
            return key_int % self.size
        return key % self.size

    def keys(self):
        return [elem.key for elem in self.tab if elem is not None]

    def search(self, key):
        if key in self.keys():
            for elem in self.tab:
                if elem is None:
                    continue
                else:
                    if elem.key == key:
                        return elem.value
        return None

    def insert(self, key, value):
        if len(self.keys()) == self.size:
            if key not in self.keys():
                print("Brak miejsca!")
            else:
                i = 0
                for element in self.tab:
                    if element is None:
                        i += 1
                        continue
                    else:
                        if element.key == key:
                            self.tab[i] = Element(key, value)
                    i += 1
        if key in self.keys():
            i = 0
            for element in self.tab:
                if element is None:
                    i += 1
                    continue
                else:
                    if element.key == key:
                        self.tab[i] = Element(key, value)
                i += 1
        else:
            for i in range(self.size):
                index_where_we_add = (self.hash(key) + self.c1 * i + self.c2 * i ** 2) % self.size
                if self.tab[index_where_we_add] is None:
                    self.tab[index_where_we_add] = Element(key, value)
                    break

    def remove(self, key):
        if key in self.keys():
            i = 0
            for element in self.tab:
                if element is not None:
                    if element.key == key:
                        self.tab[i] = None
                        break
                i += 1
        else:
            print("Brak danej!")

    def __str__(self):
        if self.tab.count(None) == self.size:
            return "{}"
        string = "{"
        i = 0
        for elem in self.tab:
            if i == self.size - 1:
                string += elem.__str__() + "}"
            else:
                string += f"{elem.__str__()}, "
            i += 1
        return string


def test1(size, c1, c2):
    hashTable = HashTable(size, c1, c2)
    for key_ in range(1, 16):
        if key_ == 6:
            j = 18
            hashTable.insert(j, chr(64 + key_))
        elif key_ == 7:
            j = 31
            hashTable.insert(j, chr(64 + key_))
        else:
            hashTable.insert(key_, chr(64 + key_))
    print(hashTable)
    print(hashTable.search(5))
    print(hashTable.search(14))
    hashTable.insert(5, 'Z')
    print(hashTable.search(5))
    hashTable.remove(5)
    print(hashTable)
    print(hashTable.search(31))
    hashTable.insert("test", 'W')
    print(hashTable)


def test2(size, c1, c2):
    hashTable = HashTable(size, c1, c2)
    for key_ in range(1, 16):
        i = key_ * 13
        hashTable.insert(i, chr(64 + key_))
    print(hashTable)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test1(13, 1, 0)
    test2(13, 1, 0)
    test2(13, 0, 1)
    test1(13, 0, 1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
