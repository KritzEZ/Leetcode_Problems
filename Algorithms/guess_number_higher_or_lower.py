class Solution(object):
    def guessNumber(self, n):
        l, r, ans = 1, n, 1
        while l<=r:
            mid = (l+r)//2
            if guess(mid) == 1:
                l = mid+1
            else:
                r = mid-1
                ans = mid

        return ans