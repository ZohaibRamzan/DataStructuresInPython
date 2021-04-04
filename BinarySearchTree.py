class BinarySearchNode():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
# Add child to the tree asper value
    def add_child(self,data):
        if data==self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)  # recursive call
            else:
                self.left=BinarySearchNode(data)  # newly added node with value data
        else:
            if self.right:
                self.right.add_child(data)  # recursive call
            else:
                self.right = BinarySearchNode(data)  # newly added node with value data
# find minimum value in binary search Tree
    def find_min(self):
        if self.left==None:
            return self.data
        else:
            left_elements = self.In_order_Traversal()
        return left_elements[0]

    # find max value in binary search Tree
    def find_max(self):
        if self.right==None:
            return self.data
        else:
            left_elements = self.In_order_Traversal()
        return left_elements[-1]


# Binary Search Tree Traversal Techniques 1-In order traversal,  2- pre-order traversal 3- post-order traversal
# In-order traversal produces ascending sorted list(set)
    def In_order_Traversal(self):
         elements=[]
         # visit left sub_tree
         if self.left:
             elements+=self.left.In_order_Traversal()
         # base node
         elements.append(self.data)
         # visit right subtree
         if self.right:
             elements+=self.right.In_order_Traversal()

         return elements

# pre-order traversal
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
# post-order traversal
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
# Search for value in Binary Search Tree,True/False
    def Search_Value(self,value):
        if self.data==value:
            return True
        if value < self.left.data:
            self.left.Search_Value(value)
        else:
            return False
        if value > self.right.data :
            self.right.Search_Value(value)
        else:
            return False
# reverse Binary Search Tree

    def invertTree(self):

        if self:
            self.left , self.right= self.right.invertTree() , self.left.invertTree()
            return self


def create_binary_search_tree(array):
    root= BinarySearchNode(array[0])
    for element in array[1:]:
        root.add_child(element)

    return root



if __name__ == '__main__':
    numbers=[12,43,65,89,100,33,12,15,7]
    colors=['green','red','yellow','pink']
# In order traversal check
    number_tree=create_binary_search_tree(numbers)
    new_number_tree=number_tree
    result=number_tree.In_order_Traversal()
    print('In-order-Traversal result on numbers is: ',result)
# check on strings
    color_tree = create_binary_search_tree(colors)
    result = color_tree.In_order_Traversal()
    print('In-order-Traversal result on strings is: ', result)

# check if vvalue is found in binary search tree
    number=12
    print('number {} is found: {}'.format(number,new_number_tree.Search_Value(number)))

# Exercise Solutions
# find minimum value in Binary Search Tree
    print('Minimum number in tree is: ',new_number_tree.find_min())
# find max value in Binary Search Tree
    print('Max number in tree is: ',new_number_tree.find_max())
    result = number_tree.pre_order_traversal()
    print('pre-order-Traversal result on numbers is: ', result)

# inverse tree
    new_number_tree.invertTree()
    result = new_number_tree.In_order_Traversal()
    print('In-order-Traversal result on numbers is: ', result)







