class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = float('inf')
        dp = [[inf] * (len(coins)+1) for i in range(amount+1)]
        for i in range(len(coins)+1):
            dp[0][i] = 0
        for i in range(1,amount+1):
            for j in range(1, len(coins)+1):
                dp[i][j] = dp[i][j-1] 
                if i -coins[j-1] >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - coins[j-1]][j]+1)  
        if dp[amount][len(coins)] == inf:    
            return -1 
        else:
            return dp[amount][len(coins)]