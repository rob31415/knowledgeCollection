#!/usr/bin/python3
# -*- coding: utf-8 -*-

# wip: doesn't work yet

# binary search tree

class bstNode:
	value = None
	parent = None
	left = None
	right = None
	def __init__(self, value):
		self.value = value


def bstInsert(root, node):
	if(root == None):
		root = bstNode(node.value)
		return root
	else:
		if(node.value > root.value):
			root.right = bstInsert(root.right, node)
		else:
			root.left = bstInsert(root.left, node)

a = bstNode(10)
#print(a.value)
#b = bstNode(2)
#a.right = b
#print(a.value)
bstInsert(a, bstNode(9))
bstInsert(a, bstNode(11))
bstInsert(a, bstNode(12))
print(a.right.value)
