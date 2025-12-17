from typing import List, Tuple


def lcs(string_1: str, string_2: str) -> str:
    """Ищет самую длинную последовательность символов, 
    которая встречается в заданном порядке в обеих строках.
    """
    if not string_1 or not string_2:
        return ""

    m, n = len(string_1), len(string_2)
    dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string_1[i - 1] == string_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    result: List[str] = []
    while i > 0 and j > 0:
        if string_1[i - 1] == string_2[j - 1]:
            result.append(string_1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))

