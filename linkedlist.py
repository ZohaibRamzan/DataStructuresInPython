# The Code is written to revise Data Structures for python Language
# Below code is for LinkedList Data Structure
# Big(O) for insert at start and end is O(1)
# Advantage of linkedlist over Array is it expends(add new element) as the requirement increases
class Node:
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head= None

 # insert element to linkedlist
    def add_element(self, data):
        node=Node(data,self.head)
        self.head=node
        return
 # remove the element as per index value 
    def remove_at_index(self,index):
        leng=self.get_length()
        #print(leng)
        itr=self.head
        for i in range(leng):
            if i==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
          
# reverse linkedlist
        def reverse_ll(self):
        itr=self.head
        arr=[]
        while itr:
            arr.append(itr.data)
            itr=itr.next
        b = linkedlist()
        for element in arr:
            print(element)
            b.insert_element((element))
        b.print_ll()
        
# list to linkedlist 
    def List_to_ll(self, arr):
        for ele in arr:
            self.insert_at_end(ele)


# insert element at end of linkedlist
    def insert_at_end(self,data):
        if self.head==None:   # means empty object
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)


    def print_ll(self):
        if self.head==None:
            print('Linked list is empty')
            return
        itr=self.head
        linked_list=''
        while itr:
            linked_list+=str(itr.data)+ '--->'
            itr=itr.next
        print(linked_list)
        
# get length of linkedlist
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def insert_at(self,index,elem):
        if index==0:
            node=Node(elem,self.head)
            self.head=node
        itr= self.head
        leng=self.get_length()
        for i in range(leng):
            if i == index - 1:
                itr.next = Node(elem,itr.next)
            itr = itr.next
# Exercise Solutions
    def remove_by_value(self, value):
        itr=self.head
        index=0
        while itr:
            if itr.data==value:
                self.remove_at_index(index)
                break
            index+=1
            itr=itr.next

    def insert_after_value(self,data, data_after):
        itr=self.head
        while itr:
            if itr.data==data:
                itr.next=Node(data_after,itr.next)
                break
            itr=itr.next


if __name__=="__main__":
    a=linkedlist()
    a.add_element(12)
    a.add_element(34)
    a.print_ll()
    a.insert_at_end(100)
    a.print_ll()
    numbers=[12,23,54,65]
    b=linkedlist()
    b.List_to_ll(numbers)
    b.print_ll()
    length=b.get_length()
    print('length',length)
    b.remove_at_index(1)
    b.print_ll()
    b.insert_at(1,344)
    b.print_ll()


    ### Exercise
    b.remove_by_value(54)
    b.print_ll()
    fruits=['banana','Mango','grapes','orange']
    c = linkedlist()
    c.List_to_ll(fruits)
    c.insert_after_value('Mango', 'Apple')
    c.print_ll()






