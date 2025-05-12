class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for n in range(2, len(cost)):
            dp[n] = min(dp[n-1]+cost[n], dp[n-2]+cost[n])
        
        return min(dp[len(cost)-1], dp[len(cost)-2])