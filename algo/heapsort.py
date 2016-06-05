#! /usr/bin/python3

maxHeap = []

def parentIdx(elementIdx):
	if(elementIdx == 0):
		return -1
	else:
		return int(elementIdx-1/2)

def firstChildIdx(Q, elementIdx):
	idx = (elementIdx*2)+1
	return idx if idx<len(Q) else -1

def secondChildIdx(Q, elementIdx):
	idx = firstChildIdx(Q, elementIdx)
	if(idx>-1):
		return idx+1 if idx+1<len(Q) else -1
	else:
		return idx

def swap(Q, oneIdx, anotherIdx):
	if(oneIdx != anotherIdx):
		tmp = Q[oneIdx]
		Q[oneIdx] = Q[anotherIdx]
		Q[anotherIdx] = tmp
		return True
	return False

def bubbleUp(Q, elementIdx):
	if(parentIdx(elementIdx) == -1):
		return
	else:
		# < for minheap
		if(Q[elementIdx] > Q[parentIdx(elementIdx)]):
			swap(Q, elementIdx, parentIdx(elementIdx))
			bubbleUp(Q, parentIdx(elementIdx))


def getIdxOfMaxVal(Q, idx1, idx2, idx3):
	idx = idx1
	# < for minheap
	if(idx2 > -1 and Q[idx2] > Q[idx]):
		idx = idx2
	# < for minheap
	if(idx3 > -1 and Q[idx3] > Q[idx]):
		idx = idx3
	return idx

def bubbleDown(Q, elementIdx):
	firstChild = firstChildIdx(Q, elementIdx)
	secondChild = secondChildIdx(Q, elementIdx)
	swapWithIdx = getIdxOfMaxVal(Q, elementIdx, firstChild, secondChild)
	#print(Q[elementIdx], firstChild, secondChild, swapWithIdx)
	if(swap(Q, elementIdx, swapWithIdx)):
		bubbleDown(Q, swapWithIdx)

def insert(Q, element):
	Q.append(element)
	bubbleUp(Q, len(Q)-1)

def extractMax(Q):
	if(len(Q)>0):
		max = Q[0]
		if(len(Q)>1):
			Q[0] = Q.pop()
			bubbleDown(Q, 0)
		else:
			Q.pop()
		return max
	else:
		return -1


insert(maxHeap, 1)
insert(maxHeap, 6)
insert(maxHeap, 9)
insert(maxHeap, 3)
insert(maxHeap, 2)
insert(maxHeap, 3)
print(maxHeap)

while len(maxHeap)>0:
	print(extractMax(maxHeap))
	print(maxHeap)
