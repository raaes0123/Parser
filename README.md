# Builds the parse tree recursively
# (pgm1 -i arg < myfile | pgm2) ; pgm3 arg3
# Start with the highest precedence (Sequence (;, |, <, >))
# Sequence has left subtree and right subtree
# Left subtree: Search for the operator with least precedence ie group ()
# Within the group go through the same process
# Specifically the lowest precedence within the group is pipe (|)
# Build the left subtree which w

# Precedence from lowest to highest
# Sequence (;)
# Group ()
# Pipe |
# Redir <,>
