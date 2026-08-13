class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        return [val[0] for val in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]]
                    
        
        
