class Solution:
    def dfs(self, row, col):
        if not self.validPosition(row, col):
            return 0
        if self.atEndPosition(row, col):
            return 1

        self.grid[row][col] = 1
        paths = 0
        paths += self.dfs(row + 1, col)
        paths += self.dfs(row - 1, col)
        paths += self.dfs(row, col + 1)
        paths += self.dfs(row, col - 1)
        self.grid[row][col] = 0
        return paths

    def validPosition(self, row, col):
        valid_row = 0 <= row < self.num_rows
        valid_col = 0 <= col < self.num_cols
        return valid_row and valid_col and self.grid[row][col] == 0
    
    def atEndPosition(self, row, col):
        return (row == self.num_rows - 1) and (col == self.num_cols - 1)

    def countPaths(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        self.num_rows, self.num_cols = len(grid), len(grid[0])
        self.grid = grid
        return self.dfs(0, 0)


        