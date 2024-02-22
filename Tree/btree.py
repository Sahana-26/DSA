class node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

newBT= node("friuts")
leftchild= node("red")
rightchild= node("green")
appple= node("apple")
st= node("strawberry")
newBT.leftchild=leftchild
newBT.rightchild=rightchild
leftchild.leftchild=appple
leftchild.rightchild=st



def preorder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorder(rootNode.leftchild)
    preorder(rootNode.rightchild)
preorder(newBT)

def inorder(rootNode):
    if not rootNode:
        return
    preorder(rootNode.leftchild)
    print(rootNode.data)
    preorder(rootNode.rightchild)
inorder(newBT)

def level_order(index):
    for i in range(index,self.lastUsedIndex+1):
        print(self.customList[i])
    

level_order(1)