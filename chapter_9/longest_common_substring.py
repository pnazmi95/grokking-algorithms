dp_table_blue = ["b", "l", "u", "e"]
# dp_table_blue = ["H", "I", "S", "H"]
dp_table_clues = ["c", "l", "u", "e", "s"]
# dp_table_clues = ["F", "I", "S", "H"]
dp_table = [[0 for i in range(len(dp_table_blue))] for i in range(len(dp_table_clues))]
# (5,4)
print(dp_table)

for i in range(len(dp_table_blue)):
    for j in range(len(dp_table_clues)):
        if dp_table_blue[i] == dp_table_clues[j]:
            dp_table[i][j] = dp_table[i - 1][j - 1] + 1

print(dp_table)
