# 动态规划
# https://www.cnblogs.com/nullzx/p/10991305.html
"""
1. 将一个规模较大的问题转换成一个或若干个规模较小的子问题，可以将其处理成递归的方式
2. 使用递归效率较低，可以用空间换时间，建立一张表，记录每一个子问题的结果。填表的过程与递归的过程正好相反
"""

# 1. 斐波那契数列
# f(n) = f(n-1) + f(n-2)
# f3 = f2 + f1
"""
# 递归调用
def fbnq_digui(n: int) -> int:
	if n < 0:
		return 0
	if n == 1 or n == 2:
		return 1
	return fbnq_digui(n-1) + fbnq_digui(n-2)

for i in range(1, 10):
	print("i = {}, value = {}".format(i, fbnq_digui(i)))

# for循环调用，计算的数据存在表中
def fbnq_for(n: int) -> int:
	tableL = list()
	tableL.append(0)
	tableL.append(1)
	tableL.append(1)

	for i in range(3, n+1):
		tableL.append(tableL[i-1] + tableL[i-2])
	return tableL[n]

print("v = {}".format(fbnq_for(9)))
"""

#2. 走楼梯问题
"""
1. 简化版
	楼梯有n阶，每次可以走1阶，或者2阶，有多少种走法
	f1 = 1 --> 每次走1次
	f2 = 2 --> 每次1阶，走两次；每次走2阶，走1次。
	f3 = f1 + f2 --> 每次走1阶，走3次；先走1阶，再走2阶；先走2阶，再走1阶；
"""

"""
def lt_digui(n :int) -> int:
	if n < 0:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	return lt_digui(n-1) + lt_digui(n-2)

for i in range(1, 11):
	print("i = {}, value = {}".format(i, lt_digui(i)))
	
def lt_for(n: int) -> int:
	tableL = []
	tableL.append(0)
	tableL.append(1)
	tableL.append(2)
	
	for i in range(3, n + 1):
		tableL.append(tableL[i-1] + tableL[i - 2])
	return tableL[n]
	
print("value = {}".format(lt_for(10)))
"""

#2. 走楼梯问题
"""
2. 加强版
	楼梯有n阶，每次可以走2阶，或者3阶，或者5阶，有多少种走法
	f2 = 1 --> 每次走2次
	f3 = 1 --> 每次3阶，走1次
	f5 = 3 --> 每次走5阶，走1次；先走3阶，再走2阶；先走2阶，再走3阶；
	可以拆分为f(n) = f(n-5) + f(n-3) + f(n-2)
"""
"""
def lt_digui(n: int) -> int:
	if n < 0:
		return 0
	elif n == 0:
		return 1
	return lt_digui(n-5) + lt_digui(n-3) + lt_digui(n-2)

for i in range(1, 11):
	print("i = {}, value = {}".format(i, lt_digui(i)))

def lt_for(n: int) -> int:
	tableL = []
	# 默认0 = 1
	tableL.append(1);
	for i in range(1, n + 1):
		n2 = tableL[i-2] if i - 2 >= 0 else 0
		n3 = tableL[i-3] if i - 3 >= 0 else 0
		n5 = tableL[i-5] if i - 5 >= 0 else 0
		tableL.append(n2 + n3 + n5)
	return tableL[n]
print("value = {}".format(lt_for(10)))
"""

# 3. 数塔问题
"""
问题描述：从顶部出发的每一个节点可以选择向下或者向右下走，直到走到底层，要求找出一条路径，使得路径上的数字之和最大。
32
83	68
40	37	47
5	4	67	22
79	69	78	29	63
0	71	51	82	91	64

分析：将这个大的问题拆分为两个小问题，如：
83	
40	37	
5	4	67	
79	69	78	29	
0	71	51	82	91

68
37	47
4	67	22
69	78	29	63
71	51	82	91	64
拆分成两个，然后再继续拆，直到拆到最小问题，匹配每次得到的最大值就可以


#二维数组
a = [[0],[1,1], [2,2,2], [3,3,3,3]]
for i in range(0, len(a)):
	a1 = a[i]
	for j in range(0, len(a1)):
		print("i = {}, j = {}, value = {}".format(i, j, a[i][j]))
"""

# 递归是从上往下走：
"""
def shuta_digui(a: list) -> int:
	
	# i表示行、j表示列
	def digui(a: list, i: int, j: int) -> int:
		print("i = {}, j = {}, value = {}".format(i, j, a[i][j]))
		if (i == len(a) - 1):
			return a[i][j]
		#求i+1，j的最大值
		r1 = digui(a, i+1, j)
		#求i+1，j+1的最大值
		r2 = digui(a, i+1, j+1)
		print("i={}, j={}, r1={}, r2={}".format(i, j, r1, r2))
		return a[i][j] + max(r1, r2)
	
	return digui(a, 0, 0)
"""
	
a = [[32], [83,68], [40,37,47], [5,4,67,22],[79,69,78,29,63], [0,71,51,82,91,64]]
#print(shuta_digui(a))
	
		
# 使用递归，有很大一部分数据一直在重复计算，所以还是用空间换时间
# 需要倒推，有一个与传进来的二维数组一样的变量

def shuta_for(a: list) -> int:
	dp = a
	for i in range(len(a)-1, -1, -1):
		
	



















