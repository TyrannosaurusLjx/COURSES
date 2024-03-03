# import copy

class SingleList():
    # Node class
    class node():
        def __init__(self,item) -> None:
            self.value = item
            self.next  = None
            return
        
    # SingleList class
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0
        return

    # get length
    def length(self):
        return self.len
    
    # push method
    def push(self,item):
        new_node = self.node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.len += 1
        return
   
    # insert at index i 
    def insert(self, i, item):
        if i == 0 and self.len == 0 :
            self.push(item)
            self.len += 1
            return
        elif i < 0 or i >= self.len:
            raise IndexError("index out of range ")
            return 
        elif i == 0 and self.len == 1:
            self.head = self.node(item)
            self.head.next = self.tail
            self.len += 1
            return 
        else:
            p = self.head
            for _ in range(i-1):
                p = p.next
            n = p.next
            temp = self.node(item)
            p.next = temp
            temp.next = n
            self.len += 1
            return
            
    # empty method
    def empty(self):
        return self.head == None
    
    # makeEmpty method
    def makeEmpty(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    # init method
    def init(self, item) -> bool:
        temp = self.head
        while temp != self.tail:
            if temp.value == item:
                return True 
            else:
                temp = temp.next
                # does self.tail == item ?
        return self.tail == item
    
    # pop method 
    def pop(self):
        if self.empty():
            raise IndexError("there is nothing to pop")
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        value = self.tail.value
        temp.next = None
        self.tail = temp
        self.len -= 1
        return value
   
    # get the value of index i
    def get(self,i):
        if i < 0 or i >= self.length():
            raise IndexError("Index out of range")
            return None
        else:
            temp = self.head
            for _ in range(i):
                temp = temp.next
            return temp.value

    # remove method
    # the del might be unnecessary
    def remove(self, item) -> bool:
        if self.empty():
            raise IndexError("there is nothing to remove")
        elif self.head == self.tail :
            if self.head == item:
                self.makeEmpty()
                self.len -= 1
                return True
            else:
                raise ValueError("no this value")
        else:
            p = self.head
            # if head is item
            if p.value == item:
                self.head = self.head.next
                del p
                self.len -= 1
                return True
            # the case that if tail is item will be solved after n comes to tail's preview 
            n = self.head.next
            while n != self.tail:
                if n.value == item:
                    p.next = n.next
                    del n 
                    self.len -= 1
                    return True
                else:
                    p = n
                    n = n.next
            # now n is tail which should be deleted if equals item 
            # and p.next should turn to None, since now it's tail
            if self.tail.value == item:
                p.next = None
                self.tail = p
                del n
                self.len -= 1
                return True
            raise ValueError("no this value")
                    
    # print method
    def print(self):
        if self.head == None:
            print("List is empty")
            return
        else:
            temp = self.head
            while temp != None:
                print(temp.value)
                temp = temp.next
            return

class DoubleList():
    class node():
        def __init__(self,item) -> None:
            self.value = item
            self.prior = None
            self.next = None
            return

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0
        return

    #pre method
    def pre(self, item):
        self.len += 1
        if self.head == self.tail:
            if self.head == None:
                self.head = self.node(item)
                self.tail = self.head
                return
            else:
                self.head = self.node(item)
                self.head.next = self.tail
                self.tail.prior = self.head
                return
        else:
            temp = self.node(item)
            temp.next = self.head
            self.head.prior = temp
            self.head = temp
            return


    # push method
    def push(self, item):
        self.len += 1
        if self.head == self.tail:
            if self.head == None:
                temp = self.node(item)
                self.head = temp
                self.tail = temp
                return 
            else:
                self.tail = self.node(item)
                self.head.next = self.tail
                self.tail.prior = self.head
                return
        else:
            temp = self.node(item)
            temp.prior = self.tail
            self.tail.next = temp
            self.tail = temp
            return

    # empty method
    def empty(self):
        return self.head == None

    # makeEmpty
    def makeEmpty(self):
        if self.empty():
            return
        else:
            self.head = None
            self.tail = None
            return
    # print method
    def print(self):
        if self.empty():
            print("list is empty!")
            return
        else:
            temp = self.head
            while temp != self.tail:
                print(temp.value)
                temp = temp.next
            print(temp.value)
            return

    # get length
    def length(self):
        return self.len

    # insert 
    def insert(self, index, item):
        if index == 0  and self.len == 0:
            self.push(item)
            return
        elif index == 0 and self.len == 1:
            self.pre(item)
            self.len += 1
            return
        elif index < 0 or index >= self.len:
            raise IndexError("index out of range")
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            new_node = self.node(item)
            temp.prior.next = new_node
            new_node.prior = temp.prior
            new_node.next = temp
            temp.prior = new_node
            self.len += 1
            return
    
    def look(self):
        print(self.head,self.head.value)
        print(self.tail,self.tail.value)

 
