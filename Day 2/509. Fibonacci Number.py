class Solution(object):
    def fib(self, n):
        # if n==0 or n==1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)
        ans = []
        for i in range(n+1):
            if i==0 or i==1:
                ans.append(i)
            else:
                ans.append(ans[i-1] + ans[i-2])
        return ans[n]