class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                box_index = (r//3)*3 + (c//3)
            
                if val in rows[r] or val in columns[c] or val in box[box_index]:
                    return False

                rows[r].add(val)
                columns[c].add(val)
                box[box_index].add(val)
        return True

        