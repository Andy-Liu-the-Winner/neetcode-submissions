class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        length_of_matrix = len(matrix)

        def spiral_trasverse(initial, length):
            result = []

            for i in range(length):
                result.append(matrix[initial][initial + i])

            for i in range(length):
                if i == 0 or i == length - 1:
                    continue
                result.append(matrix[initial + i][initial + length - 1])

            for i in range(length):
                result.append(
                    matrix[initial + length - 1][initial + length - 1 - i]
                )

            for i in range(length):
                if i == 0 or i == length - 1:
                    continue
                result.append(matrix[initial + length - 1 - i][initial])

            return result

        res = []

        for i in range(length_of_matrix // 2):
            res.extend(spiral_trasverse(i, length_of_matrix - 2 * i))

        if length_of_matrix % 2 != 0:
            res.append(matrix[length_of_matrix // 2][length_of_matrix // 2])

        return res