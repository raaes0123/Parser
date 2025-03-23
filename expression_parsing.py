# Parse: (3+(4*8))

# If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.

# If the current token is in the list ['+','-','/','*'], set the root value of the current node to the
# operator represented by the current token. Add a new node as the right child of the current node and
# descend to the right child.

# If the current token is a number, set the root value of the current node to the number and return to the parent.

# If the current token is a ')', go to the parent of the current node.

import operator
from treeart import *

class Node:
    def __init__(self,val=None,left=None,right=None,parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def evalExp(root):
    # Evaluate each node with the following rules
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    # If a number do nothing the val is there
    # If an operand call evalExp on the left child and right child and perform the operation
    if root:
        # Base case
        if root.val.isdigit():
            return int(root.val)
        return opers[root.val](evalExp(root.left),evalExp(root.right))
    # The final result is in root's val

def dispTree(exp):
    # exp = '+ 4 * 5 - 3 8'
    # exp = '- 3 8'
    v = exp
    if len(exp) >= 5:
        t = binary_edge(v[-3],v[-2],v[-1])
        for i in range(len(v) - 5, -1,-2):
            t = binary_edge(v[i],v[i+1],t)
    else:
        t = binary_edge(v[-3],v[-2],v[-1])
    print('\n',t)

def traverseTree(root,exp):
    if root:
        # print(root.val)
        exp.append(root.val) # + ' '
        traverseTree(root.left,exp)
        traverseTree(root.right,exp)
    return exp

def makeTree(root,cmd): 
    current_node = root
    i = 0
    while i < len(cmd):
        token = cmd[i]
        # If the current token is a '(', add a new node as the left child of the current node,
        # and descend to the left child.
        if token == '(':
            current_node.left = Node()
            # Assign parent
            current_node.left.parent = current_node
            current_node = current_node.left
        # If the current token is in the list ['+','-','/','*'], set the root value of the current node
        # to the operator represented by the current token.
        # Add a new node as the right child of the current node and descend to the right child.
        elif token in ['+','-','/','*']:
            current_node.val = token
            current_node.right = Node()
            # Assign parent
            current_node.right.parent = current_node
            current_node = current_node.right
        # If the current token is a number, set the root value of the current node to the number
        # and return to the parent.
        elif token in ['0','1','2','3','4','5','6','7','8','9']:
            current_node.val = token
            i = i + 1
            if i < len(cmd) and cmd[i] in ['0','1','2','3','4','5','6','7','8','9']:
                current_node.val = current_node.val + cmd[i]
            else:
                i = i - 1
            current_node = current_node.parent
        # If the current token is a ')', go to the parent of the current node.
        elif token == ')':
            current_node = current_node.parent
        i = i + 1

if __name__ == '__main__':
    # cmd = input().strip()
    # cmd = '(4+(4*(3-8)))'
    # cmd = '(3+1)'
    cmd = '(4+(5*(13-8)))'
    # Create a root node
    root = Node()
    makeTree(root,cmd)
    exp_list = []
    traverseTree(root,exp_list)
    for exp in exp_list:
        print(exp,end=' ')
    dispTree(exp_list)
    print("\nResult:",evalExp(root))
    