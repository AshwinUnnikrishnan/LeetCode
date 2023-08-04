class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix[0])
        
        current_sum_table = [[0] * n for _ in range(n)]
        current_element_table =  [[[] for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            current_sum_table[0][i] = matrix[0][i]
            current_element_table[0][i].append(matrix[0][i])
        
        for i in range(1,n):
            for j in range(n):
                
                # leftmost and rightmost will have two values everything else will have 3
                if j == 0:
                    min_value = current_sum_table[i-1][0]
                    min_index = 0
                    if j+1 < n:
                        if current_sum_table[i-1][1] < min_value:
                            min_index = 1
                        
                elif j == (n-1): # this already take care above when only 1 column so direct compare and take 1 value
                    min_value = current_sum_table[i-1][n-1]
                    min_index = n - 1
                    if current_sum_table[i-1][n-2] < min_value:
                        min_index = n - 2
                else:
                    min_value = current_sum_table[i-1][j-1]
                    min_index = j-1
                    for k in range(j, j+2):
                        if min_value > current_sum_table[i-1][k]:
                            min_value = current_sum_table[i-1][k]
                            min_index = k
                
                current_element_table[i][j].append(matrix[i-1][min_index])
                current_sum_table[i][j] = current_sum_table[i-1][min_index] + matrix[i][j]
        
        print(current_sum_table)
        print(current_element_table)
        min_sum = min(current_sum_table[n-1])
        
        return min_sum            