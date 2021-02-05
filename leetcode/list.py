def solution(A):
    n, m = len(A), len(A[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) * 10 + A[i - 1][j - 1]
    print(str(dp))


A = (
    (9, 9),
    (9, 7)
)

solution(A)
