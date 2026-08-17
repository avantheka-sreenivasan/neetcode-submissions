class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)

        if not nums:
            return 0

        longest = 1

        for num in nums:
            if num-1 not in nums:
                length=1
                current=num
                while current+1 in nums:
                    length+=1
                    current+=1
                    
                    
                longest = max(longest, length)

        return longest
        