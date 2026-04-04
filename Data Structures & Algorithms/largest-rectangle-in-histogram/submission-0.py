class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, h in enumerate(heights):
            left = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                left = index
            stack.append((left, h))
        for index, height in stack:
            area = max(area, height * (len(heights)- index))
        return area