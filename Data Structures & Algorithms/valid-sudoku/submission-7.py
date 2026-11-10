# Runtime Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
  
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]

                if val == '.':
                    continue

                if val in rows[i] or val in cols[j]:
                    return False

                start_row = (i // 3) * 3
                start_col = (j // 3) * 3
                for row in range(start_row, start_row+3):
                    for col in range(start_col, start_col+3):
                        if (row, col) != (i, j) and board[row][col] == val:
                            return False

                rows[i].add(val)
                cols[j].add(val)

        return True
                    

