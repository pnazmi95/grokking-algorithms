# dp_table_blue = ["b", "l", "u", "e"]
# dp_table_clues = ["c", "l", "u", "e", "s"]
# dp_table = [[0 for i in range(len(dp_table_blue))] for i in range(len(dp_table_clues))]
# # (5,4)
# print(dp_table)
#
# for i in range(len(dp_table_blue)):
#     for j in range(len(dp_table_clues)):
#         if dp_table_clues[j] == dp_table_blue[i]:
#             dp_table[j][i] = dp_table[j - 1][i - 1] + 1
#         else:
#             dp_table[j][i] = max(dp_table[j - 1][i], dp_table[j][i - 1])
#
# print(dp_table)

word_a = ["f", "i", "s", "h"]
word_b = ["f", "o", "s", "h"]
dp_table = [[0 for j in range(len(word_b))] for i in range(len(word_a))]

for i in range(len(word_a)):
    for j in range(len(word_b)):
        if word_a[i] == word_b[j]:
            dp_table[i][j] = dp_table[i - 1][j - 1] + 1
        else:
            dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

print(dp_table)
