from Trees.TreeNode import TreeNode

def inorderIteratively(root):
    stack = []
    cur = root

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        print(cur.val)
        cur = cur.right

def getTree():

    root = TreeNode(10)

    left = TreeNode(5)
    left.left = TreeNode(4)
    left.right = TreeNode(8)

    right = TreeNode(15)
    right.left = TreeNode(12)
    right.right = TreeNode(20)

    root.left = left
    root.right = right

    return root


def inorder(root, array):
    if not root:
        return

    inorder(root.left, array)
    array.append(root.val)
    inorder(root.right, array)

def kSmallest(root, k):
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right


if __name__ == '__main__':
    root = getTree()
    # inorder(root)
    # inorderIteratively(root)

    sortedArray = []
    inorder(root, sortedArray)
    print(sortedArray)
    k = 5

    print(kSmallest(root, k))



