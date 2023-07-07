class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else: 
            return False
    def push(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            return
        newnode.next=self.head
        self.head=newnode
    def pop(self):
        if self.head==None:
            return None
        popped=self.head
        self.head=self.head.next
        popped.next=None
        return popped.data
    def peek(self):
        
        if self.isempty():
            return None
        return self.head.data
    def display(self):
        iter=self.head
        if self.isempty():
            print('underflow')
        else:
            while(iter!=None):
                print(iter.data,end=" ")
                iter=iter.next
        return
if __name__=="__main__":
    d=stack()
    d.push(1)
    d.push(2)
    d.push(3)
    d.push(4)
    d.display()
    print("top element is =",d.peek())
    d.pop()
    d.display()
    print("top element is =",d.peek())