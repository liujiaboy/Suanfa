
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
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
leetcode - 3 最长子串
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

		

















