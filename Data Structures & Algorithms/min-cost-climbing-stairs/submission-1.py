class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])
        dp = [0 for i in range(n+1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n+1):
            if i == n:
                dp[i] = min(dp[i-1], dp[i-2])
            else:
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return dp[-1]

        