'''
Description
Find the kth element  from the end of the singly linkedlist

Example:
Input: [1,3,5,7,9], k = 2
Output: 7

Notes: 0 < k < lenght of linkedlist
'''

# ListNode class inherit form object class
class Node(object):
	def  __init__(self, x):
		self.val = x
		self.next = None

	def add(self, val):
		node = Node(val)
		curr = self

		if curr:
			while curr.next != None:
				curr = curr.next
			curr.next = node
		else:
			return node

		return curr

class Solution:
	def generateLinkedList(self, list):
		head = Node(list[0])

		for i in range(1,len(list)):
			head.add(list[i])

		return head

	def k2Last_recursive(self, head, k, res):
		if head:
			count,res = self.k2Last(head.next,k,res)
			count  += 1
			if count == k:
				res = head.val
			return count, res 
		else:
			return 0,res

	def k2Last_iterative(self, head, k):
		p1 = head
		p2 = head

		# move p2 to the kth element from p1
		count = k
		while count > 0:
			p2 = p2.next
			count -= 1

		while p2:
			p2 = p2.next
			p1 = p1.next

		return p1.val

if __name__ == '__main__':
	linkedList = [1,3,5,7,9]
	solution = Solution()
	head = solution.generateLinkedList(linkedList)
	
	count,res = solution.k2Last_recursive(head,2,0)
	res = solution.k2Last_iterative(head,2)
	print(res)
















