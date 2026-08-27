class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = bin(n)[2:]
        count = 0

        for i in bin_str:
            if i == '1':
                count+=1
        return count

        