class Solution(object):
    def generateParenthesis(self, n):
        if n == 0:
            return [""]

        result = []
        left = right = n

        self.helper(left, right, result, "")
        return result

    def helper(self, left, right, result, singleAns):
        if left>right:
            return
        if left == 0 and right == 0:
            result.append(singleAns)
        if left:
            self.helper(left-1, right, result, singleAns+"(")
        if right:
            self.helper(left, right-1, result, singleAns+")")