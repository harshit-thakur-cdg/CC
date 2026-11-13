# Name: HARSHIT THAKUR | UID: 23BAI70435
print("Name: HARSHIT THAKUR | UID: 23BAI70435")

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Example
solution = Solution()

n = 5
print("Number of ways:", solution.climbStairs(n))