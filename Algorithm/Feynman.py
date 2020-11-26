

if word_a[i] == word_b[j]:  #两个字母相同
    cell[i][j] = cell[i-1][j-1]
else:                       #两个字母不同
    cell[i][j] = 0