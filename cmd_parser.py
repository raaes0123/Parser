# Builds the parse tree recursively
# (pgm1 -i arg < myfile | pgm2) ; pgm3 arg3
# Start with the highest precedence (Sequence (;, &&, ||))
# Sequence has left subtree and right subtree
# Left subtree: Search for the operator with least precedence ie group ()
# Within the group go through the same process
# Specifically the lowest precedence within the group is pipe (|)
# Build the left subtree which w

# Precedence from lowest to highest
# Sequence (;)
# Group ()
# Pipe ||
# Redir <,>

from treeart import *

class Node:
    def __init__(self,val=None,left=None,right=None,parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def splitCmd(cmd,root,operator):
    cmd = cmd.strip()
    # Look for sequence operators (;, ||, &&) in that order
    index = cmd.rfind(operator)
    split_found = 0
    if index != -1:
        #print(cmd[0],cmd[-1])
        # If the operator is inside a ( ) don't operate unless ( ) at the ends 
        if '(' in cmd[:index] and ')' in cmd[index+1:]:
            if cmd[0] == '(' and cmd[-1] == ')':
                print(cmd)
                split_found = 1
                root.val = operator
                left_cmd = cmd[:index].strip()
                right_cmd = cmd[index+1:].strip()
                # Assign the child nodes and parent nodes
                left = Node()
                right = Node()
                root.left = left
                root.right = right
                left.parent = root
                right.parent = root
                # Recursively call the makeTree command to build the tree
                makeTree(left_cmd,left)
                makeTree(right_cmd,right)
            else:
                return 0
        else:
            split_found = 1
            root.val = operator
            left_cmd = cmd[:index].strip()
            right_cmd = cmd[index+1:].strip()
            # Assign the child nodes and parent nodes
            left = Node()
            right = Node()
            root.left = left
            root.right = right
            left.parent = root
            right.parent = root
            # Recursively call the makeTree command to build the tree
            makeTree(left_cmd,left)
            makeTree(right_cmd,right)
    return split_found

def makeTree(cmd,root):
    split_found = 0
    split_found = splitCmd(cmd,root,';')
    if split_found == 0:
        split_found = splitCmd(cmd,root,'&')
        if split_found == 0:
            split_found = splitCmd(cmd,root,'|')
            if split_found == 0:
                split_found = splitCmd(cmd,root,'<')
                if split_found == 0:
                    split_found = splitCmd(cmd,root,'>')

    if split_found == 0:
        root.val = cmd

def traverseTree(root,exp):
    if root:
        #print(root.val, end=' ')
        exp.append(root.val)
        traverseTree(root.left,exp)
        traverseTree(root.right,exp)
    return exp

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
    print(t)

if __name__ == '__main__':
    # cmd = 'pgm1 < file1 | pgm2 & pgm3'
    # cmd = 'ls ; pwd ; date'
    # cmd = '(pgm1 ; pgm2) > file'
    cmd = 'pgm1 ; pgm2 > file'
    exp = []
    # Create a root node
    root = Node()
    makeTree(cmd,root)
    traverseTree(root,exp)
    dispTree(exp)

