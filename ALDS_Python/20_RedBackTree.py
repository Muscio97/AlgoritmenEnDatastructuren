BLACK = 1
RED = 0

class RedBlackNode:
    def __init__(self,element,left=None,right=None,colour=RED,parent = None):
        self.element = element
        self.left = left
        self.right = right
        self.colour = colour
        self.parent = parent

    def __repr__(self,nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right != None:
            s1 = self.right.__repr__(nspaces + 3)
        if self.parent:
            strp = str(self.parent.element)
        else:
            strp = ''
        if self.colour:
            kleur = 'BlACK'
        else:
            kleur = 'RED'
        s2 = s2 + ' '*nspaces + str(self.element) + ' ' + kleur + ' ' + strp + '\n'
        if self.left != None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def fixDoubleRed(self,n):
        p = n.parent              #p:parent
        if not p: # n == root
            n.colour = BLACK
            return
        if p.colour == BLACK:     # geen double red
            return
        g = p.parent              #g: grand-parent
        if g.element > p.element:
            u = g.right           #u: uncle
        else:
            u = g.left
        if u and u.colour == RED: # color-flip
            g.colour = RED
            p.colour = BLACK
            u.colour = BLACK
            self.fixDoubleRed(g)  # recursie
        else:
            if n.element < p.element < g.element: #single rotation
                gr = g.right
                g.right = RedBlackNode(g.element,parent=g,left=p.right,colour=RED)
                if p.right: p.right.parent = g.right
                g.right.right = gr
                if gr: gr.parent = g.right
                g.element = g.left.element
                g.left = g.left.left
                if g.left: g.left.parent = g
            elif n.element < p.element > g.element: #double rotation
                gl = g.left
                nl = n.left
                nr = n.right
                g.left = RedBlackNode(g.element,left=gl,right=nl,parent=g,colour=RED)
                if gl: gl.parent = g.left
                if nl: nl.parent = g.left
                g.element = n.element
                p.left = nr
                if nr: nr.parent = p
            elif n.element > p.element > g.element: #single rotation
                gl = g.left
                g.left = RedBlackNode(g.element,parent=g,right=p.left,colour=RED)
                if p.left: p.left.parent = g.left
                g.left.left = gl
                if gl: gl.parent = g.left
                g.left.colour = RED
                g.element = g.right.element
                g.right = g.right.right
                if g.right:g.right.parent = g
            elif  n.element > p.element < g.element:  #double rotation
                gr= g.right
                nr = n.right
                nl = n.left
                g.right = RedBlackNode(g.element,right=gr,left=nr,parent=g,colour=RED)
                if gr: gr.parent = g.right
                if nr: nr.parent = g.right
                g.element = n.element
                p.right = nl
                if nl: nl.parent = p

    def insert(self,e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True;

        while not found and current != None:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = RedBlackNode(e)
                parent.right.parent = parent
                self.fixDoubleRed(parent.right)
            else:
                parent.left = RedBlackNode(e)
                parent.left.parent = parent
                self.fixDoubleRed(parent.left)
        return not found

    def insertArray(self,a, low=0, high=-1):
        if len(a) == 0:
            return
        if high == -1:
            high = len(a)-1
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

    def delete(self,e):
        node = self.search(e)
        if not node:
            return False
        if not node.right or not node.left:
            node.deleteMin(e)
        else:
            minnode = node.nodeMinRightTree()
            minelement = minnode.element

            minnode.deleteMin(minelement)
            node.element = minelement
        return True

    def getSibling(self):
        p = self.parent
        if p.left == self:
            return (p.right,"right")
        else:
            return (p.left,"left")

    def deleteMin(self,e):
        print('deleteMin',e)
        if self.colour == RED: # node kan (via parent) verwijderd worden
            if self.parent.right == self:
                self.parent.right = None
            else:
                self.parent.left = None
        elif self.left: # self.left.colour == RED
            self.element = self.left.element
            self.left = None
        elif self.right: # self.right.colour == RED
            self.element = self.right.element
            self.right= None
        else:   # zoek in pad naar root een red node
                # loop:
                #    met color-flip of ratation wordt X.colour == RED
                #    X = child van X
                #    (X ligt op pad van root naar node n met n. element == e )
            current = self
            while current.parent and current.parent.colour == BLACK and current.getSibling()[0].colour == BLACK:
                current = current.parent
            if not current.parent: # current == root
                current.colour = RED # maak het achteraf zwart
                if e < current.element:
                    X = current.left
                else:
                    X = current.right
            elif current.parent.colour == RED:
                X = current
            else: #single rotation
                s,side = current.getSibling()
                p = current.parent
                sr = s.right
                sl = s.left
                if side == "right":
                    p.left = RedBlackNode(element=p.element,left = current, right = sl,colour= RED)
                    current.parent = p.left
                    sl.parent = p.left
                    p.element = s.element
                    p.right = sr
                    sr.parent = p
                else:
                    p.right = RedBlackNode(element=p.element,left = sr, right = current,colour= RED)
                    current.parent = p.right
                    sr.parent = p.right
                    p.element = s.element
                    p.left = sl
                    sl.parent = p
                X = current
            # X.parent.colour == RED
            while X.colour == BLACK:
                s,side = X.getSibling() # is altijd aanwezig, want X.parent.colour == RED
                                        # s.colour == BLACK
                p = X.parent
                if (s.left == None or s.left.colour == BLACK) and (s.right == None or s.right.colour == BLACK):
                    # color-flip
                    p.colour = BLACK
                    s.colour = RED
                elif side == "right" and s.right and s.right.colour == RED: # single rotation
                    print('************')
                    sr = s.right
                    sl = s.left
                    p.left = RedBlackNode(element=p.element,left = X, right = sl,colour= BLACK)
                    X.parent = p.left
                    if sl: sl.parent = p.left
                    p.element = s.element
                    p.right = sr
                    sr.parent = p
                    sr.colour = BLACK
                elif side == "left" and s.left and s.left.colour == RED:  # single rotation
                    sr = s.right
                    sl = s.left
                    p.right = RedBlackNode(element=p.element,left = sr, right = X,colour= BLACK)
                    X.parent = p.right
                    if sr: sr.parent = p.right
                    p.element = s.element
                    p.left = sl
                    sl.parent = p
                    sl.colour = BLACK
                elif side == "right" and s.left.colour == RED: # double rotation
                    R = s.left
                    p.left = RedBlackNode(element=p.element,left = X, right = R.left,colour= BLACK)
                    X.parent = p.left
                    if R.left: R.left.parent = p.left
                    s.left = R.right
                    if R.right: R.right.parent = s
                    p.element = R.element
                elif side == "left" and s.right.colour == RED: # double rotation
                    R = s.right
                    p.right = RedBlackNode(element=p.element,left = R.right, right = X,colour= BLACK)
                    X.parent = p.right
                    if R.right: R.right.parent = p.right
                    s.right = R.left
                    if R.left: R.left.parent = s
                    p.element = R.element
                X.colour = RED
                if e < X.element:
                    X = X.left
                if e > X.element:
                    X = X.right
                # X.parant.colour == RED
            # X.element == e
            assert X.element == e
            p = X.parent
            if p.left == X:
                p.left = None
            else:
                p.right = None

    def nodeMinRightTree(self):
        if self.right:
            current = self.right
            while current.left != None:
                current = current.left
            return current
        else:
            return self

    def makeblack(self): # voor testen, maakt de hele boom zwart
        self.colour = BLACK
        if self.left: self.left.makeblack()
        if self.right: self.right.makeblack()

class RedBlackTree:
    def __init__(self,a=None):
        if a == None or len(a) == 0:
            self.root = None
        else:
            mid = len(a)//2
            self.root = RedBlackNode(a[mid],colour=BLACK)
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
            return self.root.search(e);

    def insert(self,e):
        if e == None:
            return False
        if self.root == None:
            self.root = RedBlackNode(e,colour=BLACK)
            return True
        else:
            return self.root.insert(e);

    def delete(self,e):
        if e == None or self.root == None:
            return False;
        else:
            if self.root.element == e and not self.root.left and not self.root.right:
                self.root = None
            else:
                b = self.root.delete(e)
                if self.root.colour == RED:
                    self.root.colour = BLACK
                return b

    def makeblack(self): # voor testen, maakt de hele boom zwart
        if self.root:
            self.root.makeblack()

import random

if __name__ == '__main__':
    b = RedBlackTree()
    for i in range(1,31):
        j = random.randint(1,100)
        print(j)
        b.insert(j)
        print(b)
        print('----------------')

##    b = RedBlackTree()
##    for i in [3,1,12,11,10,9,8]:
##        b.insert(i)
##        print(b)
##        print('----------------')
##    b.delete(12)
##    print('delete',12)
##    print(b)
##    print('----------------')
##
##    b = RedBlackTree(list(range(1,21)))
##    print(b)
##    print('----------------')
##
##    b.delete(16)
##    print(b)
    print('----------------')

    b = RedBlackTree()
    b.insert(10)
    b.insert(5)
    b.insert(15)
    b.insert(3)
    b.insert(8)
    b.insert(12)
    b.insert(17)

    b.insert(2)
    b.insert(4)
    b.insert(6)
    b.insert(9)
    b.insert(11)
    b.insert(13)
    b.insert(16)
    b.insert(18)
    print(b)
    print('----------------')

    b.makeblack()
    print(b)
    print('----------------')

#    b.delete(2)
    b.delete(18)
    print(b)
    print('----------------')
    b.delete(15)
    print(b)
    print('----------------')
    b.delete(17)
    print(b)
    print('----------------')
##    print('delete',8)
##    b.delete(8)
##    print(b)
##    print('----------------')
##    print('delete',10)
##    b.delete(10)
##    print(b)
##    print('----------------')
##    print('delete',7)
##    b.delete(7)
##    print(b)
##    print('----------------')
##    print('delete',9)
##    b.delete(9)
##    print(b)
##    print('----------------')
##


##    b = RedBlackTree([1,2,3])
##    print(b)
##    print('----------------')
##    b = RedBlackTree([1,2,3,4])
##    print(b)
##    print('----------------')
##    b = RedBlackTree([1,2,3,4,5,6,7,8,9,10])
##    print(b)
##    print('----------------')

##    b = RedBlackTree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
##    print(b)
##    node = b.search(3)
##    if node != None:
##        print(node.element)
##    node = b.search(4)
##    if node != None:
##        print(node.element)
##    node = b.search(8)
##    if node != None:
##        print(node.element)
##    node = b.search(11)
##    if node != None:
##        print(node.element)
##    node = b.search(16)
##    if node != None:
##        print(node.element)
##    b.insert(17);
##    print(b)
##    print('----------------')
####    b.delete(14)
####    print(b)
####    print('----------------')
##
##    print(b.insert(10))
##
##    b = RedBlackTree()
##    for i in range(1,11):
##        b.insert(i)
##    print(b)
##    print('----------------')
##
##    b = RedBlackTree(None)
##    print(b)
##    print('----------------')
##    b = RedBlackTree([])
##    print(b)
##    print('----------------')
##    b = RedBlackTree([0])
##    print(b)
##    print('----------------')
##
##    b = RedBlackTree()
##    b.insert(3)
##    b.insert(2)
##    b.insert(10)
##    b.insert(11)
##    b.insert(9)
##    b.insert(6)
##    b.insert(7)
##    b.insert(8)
##    print(b)
##    print('----------------')
####    b.delete(3)
####    print(b)
####    print('----------------')
##
