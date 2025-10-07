class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = n
        sum, prod = 0,1
        while temp>0:
            r = temp % 10
            sum = sum + r
            prod = prod * r
            temp = temp // 10
        diff = prod - sum
        return diff