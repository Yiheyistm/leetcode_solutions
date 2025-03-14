# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findInorderSuccessor(node):
            while node.left:
                node = node.left
            return node
    
        def delNode(node, key):
            if not node:
                return node 

            # Traverse the tree to find the node to delete
            if key < node.val:
                node.left = delNode(node.left, key)
            elif key > node.val:
                node.right = delNode(node.right, key)
            else:
                # Node found to delete
                if not node.left:
                    # Case 1: No Left child
                    return node.right
                elif not node.right:
                    # Case 2: No Right child
                    return node.left
                else:
                    # Case 3: The node has right and left child
                    # Finding inorder successor (smallest on the right of the tree)
                    temp = findInorderSuccessor(node.right)
                    node.val = temp.val

                    node.right = delNode(node.right, temp.val)
            return node
            
        return delNode(root, key)
        