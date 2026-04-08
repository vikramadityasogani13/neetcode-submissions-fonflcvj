class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        def backtrack(openN, closeN):
            if openN == n and closeN == n:
                result.append("".join(path))
                return
            if openN < n:
                path.append("(")
                backtrack(openN + 1, closeN)
                path.pop()
            
            if closeN < openN:
                path.append(")")
                backtrack(openN, closeN + 1)
                path.pop()

        backtrack(0, 0)
        return result