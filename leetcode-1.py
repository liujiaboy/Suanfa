
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(l: list) -> ListNode:
	header = current = ListNode()
	for i in range(0, len(l)):
		current.next = current = ListNode(l[i])
	return header.next

def printList(l: ListNode):
	while l:
		print(l.val)
		l = l.next
	print(" ")

'''
leetcode - 2 两数相加
# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
	header = current = ListNode()
	plus = val = 0
	while plus or l1 or l2:
		val = plus
		if l1:
			l1, val = l1.next, l1.val + val
		if l2:
			l2, val = l2.next, l2.val + val
		if val >= 10:
			plus, val = 1, val - 10
		else:
			plus = 0
		current.next = current = ListNode(val)
	return header.next
	
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

listno1 = createList(l1)
listno2 = createList(l2)
printList(listno1)
printList(listno2)

list3 = addTwoNumbers(listno1, listno2)
printList(list3)

'''

'''
#leetcode - 3 最长子串
def lengthOfLongestSubstring(s: str) -> int:
	if len(s) == 0:
		return 0
	
	tempS = []
	maxL = 0
	for c in s:
		if c in tempS:
			tempS[:] = tempS[tempS.index(c) + 1: ]
		tempS.append(c)
		maxL = maxL if maxL > len(tempS) else len(tempS)
	return maxL
	
print(lengthOfLongestSubstring("aabaab!bb"))
'''

'''
def isPalindrome(x: int) -> bool:
	if x < 0 or (x % 10 == 0 and x != 0):
		return False
	
	leftV, rightV = x, 0
	while leftV > rightV:
		rightV = rightV * 10 + leftV % 10
		leftV = int(leftV / 10)
	return leftV == rightV or leftV == int(rightV/10)

print(12 % 10)
print(isPalindrome(0))
'''


"""
def deleteDuplicates(head: ListNode) -> ListNode:
	num = []
	headL = l = ListNode()
	while head:
		if head.val not in num:
			num.append(head.val)
			l.next = l = ListNode(head.val)
		head = head.next	
	return headL.next

l1 = createList([1,1,2,3,3])
printList(l1)

printList(deleteDuplicates(l1))
"""


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

#[1,null,2,3]
def createTreeNode() -> TreeNode:
#	l3 = TreeNode(3)
#	l2 = TreeNode(2, l3)
#	l1 = TreeNode(1)
#	l1.right = l2
#	return l1
#		1
#	4		3
#	  2
	l1 = TreeNode(1)
	l2 = TreeNode(4)
	l3 = TreeNode(3)
	l4 = TreeNode(2)
	l1.left = l2
	l1.right = l3
	l2.right = l4
	return l1

#中序遍历
def inorderTraversal(root: TreeNode) -> []:
	tempL = []
	intL = []
	while root or len(tempL):
		while root:
			tempL.append(root)
			root = root.left

		root = tempL.pop()
		intL.append(root.val)
		root = root.right
	return intL


"""
# 先序 递归调用
def xianxu(root: TreeNode) -> []:
	
	def bianli(node: TreeNode):
		if not node: return
		intL.append(node.val)
		bianli(node.left)
		bianli(node.right)

	intL = []	
	bianli(root)
	return intL
"""

"""
# 先序 使用队列思想
def xianxu(root: TreeNode) -> []:
	nodeL = []
	intL = []
	
	while root or len(nodeL):
		while root:
			nodeL.append(root)
			intL.append(root.val)
			root = root.left
		root = nodeL.pop()
		root = root.right
		
	return intL
"""

"""
# 后续遍历：左 右 中
def houxu(root: TreeNode) -> []:
	nodeL = []
	intL = list()
	prev = None
	while root or len(nodeL):
		while root:
			nodeL.append(root)
			root = root.left
			
		root = nodeL.pop()
		if not root.right or prev == root.right:
			intL.append(root.val)
			prev = root
			root = None
		else:
			nodeL.append(root)
			root = root.right
		
	return intL
	

L = createTreeNode()
print(houxu(L))
"""

"""
# 链表反转
l1 = [1,2,3,4,5,6,7, 8, 9]

listno1 = createList(l1)
		
def fanzhuan(l: ListNode) -> ListNode:
	header = current = ListNode()
	while l:
		l1 = ListNode(l.val)
		l1.next = header.next
		header.next = l1
		l = l.next
	return header.next

#printList(fanzhuan(listno1))
"""

# LRU缓存机制
class DlinkedNode:
	def __init__(self, key = 0, value = 0):
		self.key = key
		self.value = value
		self.pre = None
		self.next = None
		
class Solution:
	cache = dict()
	# 可以使用双向链表来实现，这里取巧，使用list
	node = list()
	count = 0
	
	def LRU(self, operations: list, k: int) -> list:
		self.count = k
		resultL = []
		for i in range(len(operations)):
			innderL = operations[i]
			if innderL[0] == 1:
				self.set(innderL[1], innderL[2])
			elif innderL[0] == 2:
				resultL.append(self.get(innderL[1]))
		return resultL
		
		
	def set(self, key: int, value: int):
		if key in self.cache:
			#在cache中，移动到最前
			self.node.remove(key)
		# 插入最前边
		self.cache[key] = value
		self.node.insert(0, key)
		if len(self.node) > self.count:
			delkey = self.node.pop()
			self.cache.pop(delkey)

		
	def get(self, key: int) -> int:
		if key in self.cache:
			self.node.remove(key)
			self.node.insert(0, key)
			return self.cache[key]
		else:
			return -1
		

#sol = Solution()
#operations = [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]]
#print(sol.LRU(operations, 3))


"""
# 排列好的有重复数据的list，二分查找，并输出最小的值，
def search(numss: list, target: int):
	if not numss:
		return -1
	low, high= 0, len(numss)-1
	idx = -1
	while low <= high:
		mid = (low + high) // 2
		if numss[mid] < target:
			low = mid + 1
		elif numss[mid] > target:
			high = mid - 1
		else:
			idx = mid
			high = mid - 1
	return idx

#list1 = [1,2,2,4]
list1 = [-2,1,2]  #2 
print(search(list1, 2))
"""


"""
def maxLengthList(arr:[] ) -> []:
	# write code here
	# 采用队列的思路，先进先出，有重复的则移除前所有的数据
	res = []
	temp = []
	for i in arr:
		if i in temp:
			temp[:] = temp[temp.index(i) + 1 :]
		temp.append(i)
		if len(res) < len(temp):
			res = temp.copy()
	return res
	

def maxLengthList2(arr:[] ) -> int:
	# write code here
	# 采用队列的思路，先进先出，有重复的则移除前所有的数据
	temp = []
	maxL = 0
	for i in arr:
		if i in temp:
			temp[:] = temp[temp.index(i) + 1 :]
		temp.append(i)
		if maxL < len(temp):
			maxL = len(temp)
	return maxL


arr = [1,2,3,1,2,3,2,2]
arr = [2,3,4,5]
print(maxLengthList2(arr))
"""

"""
def getLessNums(tinput: [], k: int) -> []:
	for i in range(0, len(tinput)):
		minIdx = i
		minVal = tinput[i]
		for j in range(i + 1, len(tinput)):
			if minVal > tinput[j]:
				minVal = tinput[j]
				minIdx = j
		tinput[i], tinput[minIdx] = minVal, tinput[i]
		if i == k:
			break
	return tinput[0:k]
	
print(getLessNums([4,5,1,6,2,7,3,8],4))
"""

"""
这里会把B merge到A中。比如A = [1,2,3], B = [2,5,6]
调用方法会变成A=[1,2,3,0,0,0]自动扩展3个元素
然后把Bmerge到A中，最后的结果为[1,2,2,3,5,6]
"""
"""
def mergeTwoList(A:[], m: int, B:[], n:int):
	# 1. 使用双指针，这里直接使用m和n即可
	# 2. A、B从最后一个元素进行对比
	# 3. A的值比B大，则A[m-1]的值移动到最后，指针左移
	# 4. B的值比A大，则直接赋值，指针左移
	if not A or not B: return
	while m > 0 and n > 0:
		#
		if A[m-1] >= B[n-1]:
			A[m+n-1] = A[m-1]
			m -= 1
		else:
			A[m+n-1] = B[n-1]
			n -= 1
	if n > 0: A[:n] = B[:n]
	 

A = [1,2,3,0,0,0]
B = [2,5,6]
mergeTwoList(A, 3, B, 3)
print(A)
"""


def solveStr(s: str) -> str:
	# write code here
	l = list(s)
	for i in range(0, len(l) // 2):
		l[i], l[len(l)-1-i] = l[len(l)-1-i], l[i]
	return "".join(l)
print(solveStr("abcde"))