'''
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
a = Node(1)
b = Node(2)
c = Node(3)
print(c.data)

a.next = b
b.next = c
print(a.next) 
print (int(0x0000020A2D8C8A50))  #2242737113680  
print(b.next)  
print(int(0x000002A4DEE48B90))   #2907137411984
print(c.next)

'''
'''
class Node:
    def __init__(self,value):
     
        self.data = value
        self.next = None
'''
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        #create a empaty linked list
        self.head = None
        #no of node in the LL
        self.n = 0
    def __len__(self):
        return self.n
    


    #--------INSERTION FROM HEAD IN LINKED LIST -------#

    def insert_head(self, value):
        new_node = Node(value) #new node
        new_node.next = self.head  # create connection  
        self.head = new_node    # reassign head
        self.n = self.n + 1   #increment n (1 to 2 to 3 to 4 as so on )

    #---------TRAVERSE IN LINKED LIST ----------#
    def treverse (self):
        curr =  self.head
        while curr != None:
            print(curr.data)
            curr = curr.next
    def __str__(self):
        curr = self.head 
        result= ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return  result[:-2]
    
    #--------PRINT NODE IN TO TAIL IN LINKED LIST-------#
    '''
    def append(self, value):
        new_node = Node(value)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node  
    '''
    #this code is flexible because if value is NONE so when we fine the next value then NONE have no any NEXT then this is not working
    #then this code with conditions put and use while Loop this code run on evry posible situation 
    '''
    def append(self, value): #pahle ek append function bnaya 
        new_node = Node(value) # new node ko bnaya jisme node ko value di jayegi 

        if self.head is None: #agr self head yaki curr head ya node None hai to --
            self.head = new_node #self head ko new node bna do 
            self.n += 1 #jaise hi nya node add hua +1 yani increment kr dia 
        else:                    #agr khali n yani None nhi hai to hm loop chalyege aur age jayeng 
            curr = self.head 
            while curr.next is not None: #to yha hm loop chalya agr non curr node none nhi h to 
                curr = curr.next # increment ke liy ek ek print hojayega 1 2 3 4 5
            curr.next = new_node #curr next ko new node bnaya 
            self.n += 1 #jaise hi nya node add hua +1 yani increment kr dia 
    
    '''
    '''
    #------------INSERTION IN THE MIDDLE OF LINKED LIST -------#
    def insert_after(self, after, value):
        new_node = Node(value)
        curr = self.head
        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next
        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return 'item not found'
        '''

    '''
    #---------clear or EMPTY LINKED LIST DELETION -----------#
    # DELETION FROM HEAD------------#
    def clear(self):
        self.head = None
        self.n = 0 
    def delete_head(self):
        if self.head is None:
            return 'empty linked list'
        self.head = self.head.next
        self.n -= 1
    '''
    
    #------------------delete from tail--------------------#
    ''''
    def pop(self):
        if self.head is None:
            return 'empty linked list'
        if self.head.next is None:
            self.head = None
            self.n -= 1
            return
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        # curr - 2nd last node
        curr.next = None
        self.n -= 1
    
     '''
    '''
    def pop(self):

        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        #curr - 2nd last node
        curr.next = None
        self.n = self.n - 1
    '''

    '''
    def remove(self,value):

    if self.head == None:
      return 'Empty LL'

    if self.head.data == value:
      # you want to remove the head node
      return self.delete_head()

    curr = self.head

    while curr.next != None:
      if curr.next.data == value:
        break
      curr = curr.next

    # 2 cases item mil gaya
    # item nai mila
    if curr.next == None:
      # item nai mila
      return 'Not Found'
    else:
      curr.next = curr.next.next
      self.n = self.n - 1
        '''
    
    '''
    #-------- searchig i  linked list -----#
    def search(self,item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return 'Not Found'
    #----- getting in linked list -----#
    
    def __getitem__(self,index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1

        return 'IndexError'
    
                

L =  LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.search(6)
print(L)
'''



#QUESTION - what is the output of followinf function when head node of following linked list iis passed as input ?
#1->2->3->4->5

def fun(head):
    if(head==None):
        return
    if head.next.next!=None:
        print(head.data," ",end='')
        fun(head.next)
    print(head.data," ",end='')
LinkedList=[1,2,3,4]
print (LinkedList)