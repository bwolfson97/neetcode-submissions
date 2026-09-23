
class Solution:
    sys.setrecursionlimit(200000)
    def solve(self, board: List[List[str]]) -> None:
        R,C = len(board),len(board[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def is_valid(r,c): return 0<=r<R and 0<=c<C and board[r][c] == 'O'
        def on_edge(r,c): return is_valid(r, c) and r in (0, R-1) or c in (0, C-1)
        def region_touches_edge(r, c, seen):
            if on_edge(r, c): return True
            for d_r,d_c in directions:
                n_r,n_c = r+d_r,c+d_c
                if is_valid(n_r, n_c) and (n_r, n_c) not in seen:
                    seen.add((n_r,n_c))
                    if region_touches_edge(n_r, n_c, seen):
                        return True
            return False
        def change_to(r, c, char):
            board[r][c] = char
            for d_r,d_c in directions:
                n_r,n_c = r+d_r,c+d_c
                if is_valid(n_r, n_c):
                    change_to(n_r, n_c, char)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    if region_touches_edge(r, c, {(r, c)}):
                        change_to(r, c, 'T')
                    else:
                        change_to(r, c, 'X')
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        