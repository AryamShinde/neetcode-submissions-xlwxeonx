class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            dist = p[0]**2 + p[1]**2
            heap.append((dist, p))

        heapq.heapify(heap)
        res = []

        while k > 0:
            res.append(heap[0][1])
            heapq.heappop(heap)
            k -= 1

        return res