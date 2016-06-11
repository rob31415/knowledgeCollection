#! /usr/bin/python3

# wip: doesn't work yet


def isSubstring(trie, aString):
	return 0

def isSuffix(trie, aString):
	return 0

def numberOfOccurrances(trie, aString):
	return 0

# substring that appears at least twice
def longestRepeatedSubstring(trie, aString):
	return 0

def buildTrie(aString):
	root = {}
	for i in range(len(aString)):
		cur = root
		print(cur)
		for c in aString[i:]:
			if c not in cur:
				cur[c]={}
			cur = cur[c]
	return root

buildTrie("abacab")


#{
#	'a': {
#		'c': {
#			'a': {'b': {}}
#		},
#		'b': {
#			'a': {
#				'c': {
#					'a': {'b': {}}
#				}
#			}
#		}
#	},
#	'c': {
#		'a': {
#			'b': {}
#		}
#	},
#    'b': {'a': 
#    	{
#    		'c': {
#    			'a': {'b': {}}
#    		}
#    	}
#    }
#}
#
#



