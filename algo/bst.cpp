// g++ bst.cpp

#include <iostream>
#include <limits>

using namespace std;

struct bstNode
{
	bstNode *left = NULL;
	bstNode *right = NULL;
	int data;
	bstNode(int data) : data(data) {}
};


// root --pointsto--> pointer[bstNode] --pointsto--> bstNode
void bstInsert(bstNode **root, bstNode *node)
{
	if(*root == NULL)
	{
		*root = node;
	}
	else
	{
		if(node->data > (*root)->data)
		{
			bstInsert(&(*root)->right, node);
		}
		else
		{
			bstInsert(&(*root)->left, node);
		}
	}
}


bstNode* bstSearch(bstNode *root, int data)
{
	if(root == NULL)
	{
		return NULL;
	}
	else
	{
		if(data > root->data)
		{
			return bstSearch(root->right, data);
		}
		else
		{
			if(data < root->data)
			{
				return bstSearch(root->left, data);
			}
			else
			{
				return root;
			}
		}
	}
}

enum ORDER {IN, PRE, POST};

void bstTraverse(bstNode* node, ORDER order)
{
	if(node != NULL)
	{
		if(order == PRE) cout << node->data << " ";
		bstTraverse(node->left, order);
		if(order == IN) cout << node->data << " ";
		bstTraverse(node->right, order);
		if(order == POST) cout << node->data << " ";
	}
}


int main()
{
	bstNode *n1 = new bstNode(10);

	bstInsert(&n1, new bstNode(12));
	bstInsert(&n1, new bstNode(9));
	bstInsert(&n1, new bstNode(11));

	cout << n1->right->left->data;		// 11
	cout << bstSearch(n1, 11);			// some address
	bstTraverse(n1, IN);

	return 0;
}

// TODO: deletion (needs parent)
// at least three things are horrible with this:
// the pointers, the null and the potential stack overflow due to recursion.
