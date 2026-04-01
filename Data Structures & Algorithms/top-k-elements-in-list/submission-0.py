class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i,0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for i, num in frequency.items():
            buckets[num].append(i)
        result = []
        for i in range(len(nums), 0, -1):
            for count in buckets[i]:
                result.append(count)
                if len(result) == k:
                    return result
        