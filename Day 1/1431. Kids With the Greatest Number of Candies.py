class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # ans = []
        # max_ = max(candies)
        # for i in candies:
        #     if i+extraCandies >= max_: 
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        # return ans
        ans = []
        max_candies = max(candies)
        for i in range(0,len(candies)):
            ans.append(candies[i] + extraCandies >= max_candies)
        return ans