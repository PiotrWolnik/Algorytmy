# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Matrix:
    def __init__(self, initiator, default_value=0):
        if isinstance(initiator, tuple):
            verses, columns = initiator
            self.__matrix = [[default_value for i in range(columns)] for j in range(verses)]
        else:
            self.__matrix = initiator

    def __getitem__(self, item):
        return self.__matrix[item]

    def __len__(self):
        return len(self.__matrix), len(self.__matrix[0])

    def __add__(self, other):
        if self.__len__()[0] != other.__len__()[0] or self.__len__()[1] != other.__len__()[1]:
            raise Exception("Matrixes need to have the same size!")
        result_matrix = self.__matrix
        for verse in range(self.__len__()[0]):
            for column in range(self.__len__()[1]):
                result_matrix[verse][column] = result_matrix[verse][column] + other[verse][column]
        return Matrix(result_matrix)

    def __mul__(self, other):
        if self.__len__()[0] != other.__len__()[1] or self.__len__()[1] != other.__len__()[0]:
            raise Exception("Only matrixes with sizes N x M and M x N can be multiplied.")

        result = [[0 for i in range(self.__len__()[0])] for j in range(self.__len__()[0])]
        for verse in range(self.__len__()[0]):
            for column in range(other.__len__()[1]):
                for extra in range(other.__len__()[0]):
                    result[verse][column] += self[verse][extra] * other[extra][column]
        return Matrix(result)

    def __str__(self):
        printed_matrix = str()
        printed_matrix += "["
        for i in range(self.__len__()[0]):
            for j in range(self.__len__()[1]):
                if j == 0 and i != 0:
                    printed_matrix += " [" + f"{self[i][j]}, "
                elif j == 0 and i == 0:
                    printed_matrix += "[" + f"{self[i][j]}, "
                elif j == self.__len__()[1]-1 and i != self.__len__()[0]-1:
                    printed_matrix += f"{self[i][j]}],\n"
                elif j == self.__len__()[1]-1 and i == self.__len__()[0]-1:
                    printed_matrix += f"{self[i][j]}]]"
                else:
                    printed_matrix += f"{self[i][j]}, "
        return printed_matrix


def transpose(matrix: Matrix) -> Matrix:
    verses, columns = matrix.__len__()
    transposed_matrix = [[0 for i in range(verses)] for j in range(columns)]
    for verse in range(columns):
        for column in range(verses):
            transposed_matrix[verse][column] = matrix[column][verse]
    return Matrix(transposed_matrix)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tab1 = Matrix([[1, 0, 2],
                   [-1, 3, 1]])
    print(transpose(tab1))
    tab2 = Matrix((2, 3), 1)
    print(tab2)
    tab3 = tab1+tab2
    print(tab3)
    tab4 = tab3*Matrix([[3, 1], [2, 1], [1, 0]])
    print(tab4)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
