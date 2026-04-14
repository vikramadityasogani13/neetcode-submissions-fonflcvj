class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []

        for i, ch in enumerate(s):
            if ch == '(':
                leftStack.append(i)
            elif ch == '*':
                starStack.append(i)
            else:
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False

        while leftStack and starStack:
            if leftStack[-1] > starStack[-1]:
                return False
            leftStack.pop()
            starStack.pop()
        return len(leftStack) == 0
