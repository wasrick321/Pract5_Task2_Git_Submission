X='AGCCCTAAGGGCTACCTAGCTT'
Y='GACAGCCTACAAGCGTTAGCTTG'


m = len(X)
n = len(Y)
LCS_table = [[0] * (n + 1) for _ in range(m + 1)]


for i in range(m + 1):
    for j in range(n + 1):
        if i == 0 or j == 0:
            LCS_table[i][j] = 0
        elif X[i - 1] == Y[j - 1]:
            LCS_table[i][j] = LCS_table[i - 1][j - 1] + 1
        else:
            LCS_table[i][j] = max(LCS_table[i - 1][j], LCS_table[i][j - 1])




lcs_length = LCS_table[m][n]




lcs = []
i = m
j = n
while i > 0 and j > 0:
    if X[i - 1] == Y[j - 1]:
        lcs.append(X[i - 1])
        i -= 1
        j -= 1
    elif LCS_table[i - 1][j] > LCS_table[i][j - 1]:
        i -= 1
    else:
        j -= 1


lcs.reverse()


print(f"Length of LCS: {lcs_length}")
print(f"LCS: {''.join(lcs)}")
