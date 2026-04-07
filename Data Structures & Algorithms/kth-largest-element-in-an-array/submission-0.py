class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k = k
        self.min_heap = nums[:]
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]