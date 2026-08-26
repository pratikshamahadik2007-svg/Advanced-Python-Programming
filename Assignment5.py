def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the actual LCS string
    i = m
    j = n
    lcs_string = []

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcs_string.append(X[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    # Reverse because LCS was constructed backwards
    lcs_string.reverse()

    return dp[m][n], ''.join(lcs_string)


# Input
X = input("Enter first sequence: ")
Y = input("Enter second sequence: ")

# Find LCS
length, sequence = lcs(X, Y)

# Display result
print("Length of LCS:", length)
print("Longest Common Subsequence:", sequence)