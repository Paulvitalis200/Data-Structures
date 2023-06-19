# Given two strings, find the length of the longest common subsequence between the two strings

# Time: O(2^(n+m)), Space: O(n+m)

def dfs(s1, s2):
    return dfsHelper(s1, s2, 0, 0)


def dfsHelper(s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0

    if s1[i1] == s2[i2]:
        return 1 + dfsHelper(s1, s2, i1 + 1, i2 + 1)

    return max(dfsHelper(s1, s2, i1+1, i2), dfsHelper(s1, s2, i1, i2+1))


# Time: O(n * m), Space: O(n + m)
def dp(s1, s2):
    N, M = len(s1), len(s2)
    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(M):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[N][M]
