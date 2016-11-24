class AVLNode:

    @staticmethod
    def rebalance(n):
        nh = n
        if n.balance() > 1:
            if n.right.balance() != -1:    # bij delete is 0 en 1 mogelijk
                # single rotate to left
                n1 = n
                n2 = n1.right
                n3 = n2.left
                n1.right = n3
                n2.left = n1
                n1.height = n1.getHeight()
                n2.height = n2.getHeight()

                nh = n2

            else:
                # double right left rotate

                n1 = n
                n2 = n1.right
                n3 = n2.left
                n4 = n3.left
                n5 = n3.right

                n1.right = n4
                n2.left = n5
                n3.left = n1
                n3.right = n2

                n1.height = n1.getHeight()
                n2.height = n2.getHeight()
                n3.height = n3.getHeight()

                nh = n3
        if n.balance() < -1:
            if n.left.balance() != 1:    # bij delete is 0 en -1 mogelijk
                # single rotate to right

                n1 = n
                n2 = n1.left
                n3 = n2.right
                n1.left = n3
                n2.right = n1

                n1.height = n1.getHeight()
                n2.height = n2.getHeight()

                nh = n2;
            else:
                # double left right rotate

                n1 = n
                n2 = n1.left
                n3 = n2.right
                n4 = n3.left
                n5 = n3.right

                n1.left = n5
                n2.right = n4
                n3.left = n2
                n3.right = n1

                n1.height = n1.getHeight()
                n2.height = n2.getHeight()
                n3.height = n3.getHeight()

                nh = n3
        return nh;

    def __init__(self,element,left,right,height):
        self.element = element
        self.left = left
        self.right = right
        self.height = height

    def __repr__(self,nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right != None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' '*nspaces + str(self.element) + " h: " + \
             str(self.height) + " b: " + str(self.balance()) + '\n'
        if self.left != None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def balance(self):
        hleft = -1
        if self.left != None:
            hleft = self.left.height
        hright = -1
        if self.right != None:
            hright = self.right.height
        return hright-hleft

    def getHeight(self):
        h1 = -1
        h2 = -1
        if self.left != None:
            h1 = self.left.height
        if self.right != None:
            h2 = self.right.height
        if h1 < h2:
            return 1 + h2
        else:
            return 1 + h1

    def insert(self,e):
        duplicate = False

        if self.element < e:
            if self.right != None:
                if self.right.insert(e):
                    self.right = AVLNode.rebalance(self.right)
                else:
                    duplicate = True
            else:
                self.right = AVLNode(e,None,None,0);
        elif self.element > e:
            if self.left != None:
                if self.left.insert(e):
                    self.left = AVLNode.rebalance(self.left)
                else:
                    duplicate = True
            else:
                self.left = AVLNode(e,None,None,0)
        else:
            duplicate = True
        if not duplicate:
            self.height = self.getHeight()
        return not duplicate

    def insertArray(self,a, low=-1, high=-1):
        if len(a) == 0:
            return
        if low == -1:
            self.insertArray(a,0,len(a)-1)
        else:
            mid = (low+high+1)//2
            self.insert(a[mid])
            if mid > low:
                self.insertArray(a,low,mid-1)
            if high > mid:
                self.insertArray(a,mid + 1,high)

    def search(self,e):
        current = self
        found = False
        while not found and current != None:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
        if found:
            return current
        else:
            return None

    def minelementRightTree(self):
        current = self.right.left
        while current.left != None:
            current = current.left
        return current.element

    def delete(self,e):
        if self.element < e:
            if self.right == None:
                return False
            b = self.right.delete(e);
            if self.right.height == -1:
                self.right = None
            else:
                self.right = AVLNode.rebalance(self.right)
        elif self.element > e:
            if self.left == None:
                return False
            b = self.left.delete(e)
            if self.left.height == -1:
                self.left = None
            else:
                self.left = AVLNode.rebalance(self.left)
        else:
            b = True
            if self.left == None and self.right == None:
                self.height = -1
            elif self.left == None:
                self.element = self.right.element
                self.right = None
            elif self.right == None:
                self.element = self.left.element
                self.left = None
            elif self.right.left == None:
                self.element = self.right.element
                self.right = self.right.right
            else:
                minelement = self.minelementRightTree()
                self.element = minelement
                self.right.delete(minelement)
                self.right = AVLNode.rebalance(self.right)

        # hoogte aanpassen
        if self.height != -1:
            self.height = self.getHeight()
        return b

class AVLTree:
    def __init__(self,a=None):
        if a == None or len(a) == 0:
            self.root = None
        else:
            mid = len(a)//2
            self.root = AVLNode(a[mid],None,None,0)
            self.root.insertArray(a[:mid])
            self.root.insertArray(a[mid+1:])

    def __repr__(self):
        if self.root == None:
            return 'null-tree'
        else:
            return str(self.root)

    def search(self,e):
        if e == None or self.root == None:
            return None
        else:
            return self.root.search(e)

    def insert(self,e):
        if e == None:
            return False
        if self.root == None:
            self.root = AVLNode(e,None,None,0)
            return True
        else:
            b = self.root.insert(e)
            self.root = AVLNode.rebalance(self.root)
            return b

    def delete(self,e):
        if e == None or self.root == None:
            return False
        else:
            b = self.root.delete(e)
            if self.root.height == -1:
                self.root = None
        if self.root != None:
            self.root = AVLNode.rebalance(self.root)
        return b

if __name__ == '__main__':
    b = AVLTree([1,2,3])
    print(b)
    print('----------------')
    b = AVLTree([1,2,3,4])
    print(b)
    print('----------------')
    b = AVLTree([1,2,3,4,5,6,7,8,9,10])
    print(b)
    print('----------------')

    b = AVLTree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    print(b)
    node = b.search(3)
    if node != None:
        print(node.element)
    node = b.search(4)
    if node != None:
        print(node.element)
    node = b.search(8)
    if node != None:
        print(node.element)
    node = b.search(11)
    if node != None:
        print(node.element)
    node = b.search(16)
    if node != None:
        print(node.element)
    b.insert(17);
    print(b)
    print('----------------')
    b.delete(14)
    print(b)
    print('----------------')

    print(b.insert(10))

    b = AVLTree()
    b.insert(6)
    b.insert(4)
    b.insert(10)
    b.insert(2)
    b.insert(8)
    b.insert(16)
    b.insert(12)
    b.insert(18)
    b.insert(14)
    print(b)
    print('----------------')

    b.delete(2)
    print(b)
    print('----------------')

    b.delete(4)
    print(b)
    print('----------------')

    b.delete(6)
    print(b)
    print('----------------')

    b.delete(8)
    print(b)
    print('----------------')

    b.delete(10)
    print(b)
    print('----------------')

    b.delete(12)
    print(b)
    print('----------------')

    b.delete(14)
    print(b)
    print('----------------')

    b.delete(16)
    print(b)
    print('----------------')

    b.delete(18)
    print(b)
    print('----------------')

    b = AVLTree()
    for i in range(10,0,-1):
        b.insert(i)
    print(b)
    print('----------------')

    b = AVLTree()
    b.insert(10)
    b.insert(8)
    b.insert(16)
    b.insert(6)
    b.insert(14)
    b.insert(18)
    b.insert(12)
    b.insert(20)
    print(b)
    print('----------------')

    b.delete(6)
    print(b)
    print('----------------')
