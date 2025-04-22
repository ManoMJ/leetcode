import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # O(k)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)  # O(log k)

        return min_heap[0]
