
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
		

sol = Solution()
operations = [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]]
print(sol.LRU(operations, 3))












