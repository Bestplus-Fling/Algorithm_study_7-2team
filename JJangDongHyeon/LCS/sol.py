import sys
sys.stdin = open('input.txt')

first_arr = list(input().strip())
second_arr = list(input().strip())

first_arr_len = len(first_arr)
second_arr_len = len(second_arr)

dp= [[0] * (second_arr_len + 1) for _ in range(first_arr_len + 1)]

for i in range(1, first_arr_len + 1):
    for j in range(1, second_arr_len + 1):
        if first_arr[i - 1] == second_arr[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j-1])

print(dp[first_arr_len][second_arr_len])