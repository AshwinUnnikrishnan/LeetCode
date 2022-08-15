class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = []
        res.append([1])
        count = 0
        for i in range(numRows-1):
            temp = []
            temp.append(1)
            for j in range(count):
                temp.append(res[count][j] + res[count][j+1])
            temp.append(1)
            res.append(temp)
            count += 1
        return res