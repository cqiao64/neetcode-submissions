class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # min vs. max possible time
        res = r # setting res equal to the max for now

        while l <= r: # while pointer is still in bounds
            m = (l+r) // 2 # find the midway point essense of Binary Search
            total_time = 0 # init total_time var
            for p in piles:
                total_time += math.ceil(float(p) / m) # iterate through piles and add the rounded of piles of       bananas over the hours 

            if total_time <= h: # if the total_time is less than the target than we need to set the new res and also move the right pointer to our midway point because if it's less than we can disregard the values to the right
                res = m
                r = m - 1
            else: # if it's greater than we disregard the values to the left move the left pointer up
                l = m + 1
        
        return res # return res when pointer(s) is out of bounds