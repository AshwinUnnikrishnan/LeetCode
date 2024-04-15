class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)  # Add a sentinel at the end to handle increasing sequences until the end

            for i, h in enumerate(heights):
                while stack and h < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

            return max_area
        
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[int(matrix[0][j]) for j in range(cols)]]

        for i in range(1, rows):
            dp_row = [0] * cols
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp_row[j] = dp[i - 1][j] + 1
            dp.append(dp_row)

        max_area = 0
        for row in dp:
            max_area = max(max_area, largestRectangleArea(row))

        return max_area
        