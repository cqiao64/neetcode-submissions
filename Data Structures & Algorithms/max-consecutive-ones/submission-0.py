class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        max_streak = 0
        for i in nums:
            if i == 1:
                current += 1
                if current > max_streak:
                    max_streak = current
            else:
                if current > max_streak:
                    max_streak = current
                current = 0
        return max_streak

            


        