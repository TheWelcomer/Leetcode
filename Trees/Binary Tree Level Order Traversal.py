
def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    result = []
    frontier = collections.deque([root])
    newFrontier = collections.deque()
    while frontier != collections.deque():
        addBuffer = []
        for node in frontier:
            addBuffer.append(node.val)
        result.append(addBuffer)
        while frontier != collections.deque():
            element = frontier.popleft()
            if element.left != None:
                newFrontier.append(element.left)
            if element.right != None:
                newFrontier.append(element.right)
        while newFrontier != collections.deque():
            element = newFrontier.popleft()
            frontier.append(element)
    return result

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
#Create a tree with values: [3,9,20,null,null,15,7]


print(levelOrder())