class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
        # If the current cell is out of bounds or doesn't match the current character of the word
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            # If the entire word has been found
            if k == len(word) - 1:
                return True
            # Mark the current cell as visited by replacing its character
            temp, board[i][j] = board[i][j], '/'
            # Explore neighboring cells recursively
            found = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # Restore the character of the current cell
            board[i][j] = temp
            return found

        # Iterate over each cell in the grid to start the search
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False