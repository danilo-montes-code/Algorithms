from collections import deque

class TreeNode:

    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right



def BFS(root: TreeNode, target: int) -> bool:
    if not root:
        return False
    
    queue = deque([root])

    while queue:
        node = queue.popleft()
        
        if node.value == target:
            return True
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False

root1 = TreeNode(2,
            TreeNode(1),
            TreeNode(3)
        )
print(BFS(root1, 1))
print(not BFS(root1, 4))