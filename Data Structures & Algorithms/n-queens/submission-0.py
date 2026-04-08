class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]
        col = set()
        positiveDiagnol = set()
        negativeDiagnol = set()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in positiveDiagnol or (r - c) in negativeDiagnol:
                    continue
                
                col.add(c)
                positiveDiagnol.add(r + c)
                negativeDiagnol.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                positiveDiagnol.remove(r + c)
                negativeDiagnol.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return result