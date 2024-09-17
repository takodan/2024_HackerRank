class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        # Write your code here
        # print(root.data)
        if root.left:
            l_height = self.getHeight(root.left) + 1
        else:
            l_height = 0

        if root.right:
            r_height = self.getHeight(root.right) + 1
        else:
            r_height = 0

        return max(l_height, r_height)

        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       