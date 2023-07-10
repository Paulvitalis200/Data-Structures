def longest_subsequence(text1, text2):

    N, M = len(text1), len(text2)
    # initialize our 2d grid with M+1 columns and N+1 rows
    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(M):
            if text1[i] == text2[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    return dp[N][M]


print(longest_subsequence("abcde", "ace"))
