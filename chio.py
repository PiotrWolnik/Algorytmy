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


def chio_method(matrix_: Matrix) -> float:
    if matrix_.__len__()[0] != matrix_.__len__()[1]:
        raise Exception("This method applies only to square matrices")
    size = matrix_.__len__()[0]
    if size == 1:
        return matrix_.__getitem__(0)[0]
    else:
        new_matrix = [[0 for i in range(size - 1)] for j in range(size - 1)]
        if matrix_[0][0] == 0:
            index = 0
            for i in range(size):
                if matrix_[i][0] != 0:
                    index = i
                    break
                else:
                    continue
            matrix_change = [[0 for i in range(size)] for j in range(size)]
            for i in range(size):
                matrix_change[i] = matrix_[i]
            matrix_change[0], matrix_change[index] = matrix_change[index], matrix_change[0]
            for verse in range(size-1):
                for column in range(size-1):
                    new_matrix[verse][column] = matrix_change[0][0]*matrix_change[verse+1][column+1] -\
                        matrix_change[0][column+1]*matrix_change[verse+1][0]
            return -(1 / (matrix_change[0][0] ** (size - 2))) * chio_method(Matrix(new_matrix))
        else:
            for verse in range(size-1):
                for column in range(size-1):
                    new_matrix[verse][column] = matrix_[0][0]*matrix_[verse+1][column+1] -\
                        matrix_[0][column+1]*matrix_[verse+1][0]
            return (1/(matrix_[0][0]**(size-2))) * chio_method(Matrix(new_matrix))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = Matrix([
                    [5, 1, 1, 2, 3],
                    [4, 2, 1, 7, 3],
                    [2, 1, 2, 4, 7],
                    [9, 1, 0, 7, 0],
                    [1, 4, 7, 2, 2]
                    ])
    print(chio_method(matrix))
    matrix2 = Matrix([
                     [0, 1, 1, 2, 3],
                     [4, 2, 1, 7, 3],
                     [2, 1, 2, 4, 7],
                     [9, 1, 0, 7, 0],
                     [1, 4, 7, 2, 2]
                     ])
    print(chio_method(matrix2))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
