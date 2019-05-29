nodes = []
class BST():
    def __init__(self):
        self.__root = None
        self._size = 0
        
    class BSTnode():
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.parent = None
    
      
    def insert(self, key):
        z = self.BSTnode(key)
        y = None
        x = self.__root
        while (x!= None):
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
                
        z.parent = y
        if y == None:
            self.__root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
            
        nodes.append(key)
        self._size +=1
        
    def search_iterative(self,k):
        x = self.__root
        while(x != None):
            if x.key == k:
                return x.key
                print('found')
                break
            elif x.key < k:
                if x.right != None:
                    x = x.right
                else:
                    print('Not found')
                    break
            else:
                if x.left != None:
                    x = x.left
                else:
                    print('Not found')
                    break
                
    def search(self, k):
        x = self.__root
        while (x != None):
            return self.search_recursive(x, k)
    
    
    def search_recursive(self, x, k):
       	if x.key == k:
               print('Found')
               return x.key
               
        
        elif x.key < k:
            if x.right != None:
                self.search_recursive(x.right, k)
            else:
                print('Not found')
                
        else:
            if x.left != None:
                self.search_recursive(x.left, k)
                
            else:
                print('Not found')
                
    def smallestKey(self):
        if self.__root != None:
            return self.smallestKey_iterative(self.__root)
    
    def smallestKey_iterative(self, x):
        while True:
            if x.left != None:
                x = x.left
            else:
                print(x.key)
                return x.key
            
    def largestKey(self):
        if self.__root != None:
            return self.largestKey_iterative(self.__root)
    
    
    def largestKey_iterative(self, x):
        while True:
            if x.right != None:
                x = x.right
            else:
                print(x.key)
                return x.key
    def delete (self, k):
        if self.__root != None:
            return self.delete_func(self.__root, k)
        
    def delete_func (self, x, k):
        while True:
            if x.key == k:
                if x.left != None and x.right != None:
                    maxValue = self.largestKey_iterative(x.left)
                    x.key = maxValue
                    return self.delete_func(x.left, maxValue)
                
                elif x.left != None:
                    x.left.parent = x.parent
                    if x.parent.left == x:
                        x.parent.left = x.left
                    else:
                        x.parent.right = x.left
                        
                        
                elif x.right != None:
                    x.right.parent = x.parent
                    if x.parent.left == x:
                        x.parent.left == x.right
                    else:
                        x.parent.right = x.right
                else:
                    if x.parent.left == x:
                        x.parent.left = None
                    else:
                        x.parent.right = None
               
                break

            
            elif k < x.key:
                if x.left != None:
                    x = x.left
                    
                else:
                    print('Not found in tree')
                    break
                
            else:
                if x.right != None:
                    x = x.right
        
                else:
                    print('Not found in tree')
                    break
                
            
    def is_empty(self):
        return self._size == 0
    
    def size (self):
        print(self._size)
        return self._size
    
    def preorder_walk(self):
        nodes = []
        self._preorder_walk(self.__root, nodes)
        return nodes
        print(nodes)
    
    def _preorder_walk(self, subtree, nodes):
        if subtree:
            nodes.append(subtree.key)
            self._preorder_walk(subtree.left, nodes)
            self._preorder_walk(subtree.right, nodes)
        
            
    def inorder_walk(self):
        nodes = []
        self._inorder_walk(self.__root, nodes)
        return nodes
        #print(nodes)

    def _inorder_walk(self, subtree, nodes):
        if subtree:
            self._inorder_walk(subtree.left, nodes)
            nodes.append(subtree.key)
            self._inorder_walk(subtree.right, nodes) 
            
    def postorder_walk(self):
        nodes = []
        self._postorder_walk(self.__root, nodes)
        return nodes
        print(nodes)
    
    def _postorder_walk(self, subtree, nodes):
        if subtree:
            self._postorder_walk(subtree.left, nodes)
            self._postorder_walk(subtree.right, nodes)
            nodes.append(subtree.key)
            
bst = BST()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(4)
bst.insert(7)
bst.insert(9)
bst.insert(15)
bst.insert(18)
bst.insert(12)
bst.insert(19)
bst.postorder_walk()