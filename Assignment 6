def knapsack_bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
                
    return dp[n][W]


def knapsack_topdown(wt, val, W):
    memo = {}
    
    def solve(i, w):
        if i < 0 or w == 0:
            return 0
            
        if (i, w) in memo:
            return memo[(i, w)]
            
        if wt[i] > w:
            res = solve(i - 1, w)
        else:
            res = max(solve(i - 1, w), val[i] + solve(i - 1, w - wt[i]))
            
        memo[(i, w)] = res
        return res
        
    return solve(len(wt) - 1, W)


if __name__ == "__main__":
    print("-" * 50)
    print("0/1 Knapsack - Bottom-Up Approach (Tabulation)")
    print("-" * 50)
    values_1 = [60, 100, 120]
    weights_1 = [10, 20, 30]
    W_1 = 50
    print(f"Values: {values_1}")
    print(f"Weights: {weights_1}")
    print(f"Capacity: {W_1}")
    print(f"Maximum Value: {knapsack_bottom_up(values_1, weights_1, W_1)}")
    
    print("\n" + "-" * 50)
    print("0/1 Knapsack - Top-Down Approach (Memoization)")
    print("-" * 50)
    weights_2 = [2, 3, 4, 5]
    values_2 = [3, 4, 5, 6]
    W_2 = 5
    print(f"Values: {values_2}")
    print(f"Weights: {weights_2}")
    print(f"Capacity: {W_2}")
    print(f"Maximum Value: {knapsack_topdown(weights_2, values_2, W_2)}")
