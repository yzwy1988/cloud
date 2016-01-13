# coding=utf-8
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
# 列表解析，矩阵
# 把矩阵M的每个row中的row[1]，放在一个新的列表中，其结果就是一个包含了矩阵的第二列的新列表
clo = [row[1] for row in M]
print clo
# 例子：列表解析去步进坐标的一个硬编码列表和一个字符串
dia = [M[i][i] for i in [0, 1, 2]]
print dia

doubles = [c * 2 for c in 'python']
print doubles

G = (sum(row) for row in M)
print next(G)
# print G
