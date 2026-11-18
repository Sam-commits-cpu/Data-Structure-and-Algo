from linkedlistdsa.singlylinkedlist import Singlynode
from linkedlistdsa.doublylinkedlist import Doublynode
#display- O(n) - singlylinkedlist-main
def display_ll(head):
    curr=head
    elements=[]
    while curr:
        elements.append(str(curr.val))
        curr=curr.next
    print(' -> '.join(elements))    

#search - O(n)- singlylinkedlist-main
def search(head,val):
    curr=head
    while curr:
        if val==curr.val:
            return True
        curr=curr.next
    return False

def singlelinkedlist_main():
    head=Singlynode(1)
    A=Singlynode(3)
    B=Singlynode(4)
    C=Singlynode(5)

    head.next=A
    A.next=B
    B.next=C

    print(f"head-{head}")

    #transverse- O(n)
    # curr=head
    # while curr:
    #     print(curr)
    #     curr=curr.next

    print(search(head,5))
    display_ll(head)

#display - doublylinkedlist_main
def display_dl(head):
    curr=head
    elements=[]
    while curr:
        elements.append(str(curr.val))
        curr=curr.next
    print(" <-> ".join(elements))

#insertion-doublylinkedlist_main
def insert_at_begining(head,tail,val):
    new_node=Doublynode(val,next=head)
    head.prev=new_node
    return new_node,tail

#insertion-doublylinkedlist_main
def insert_at_end(head,tail,val):
    new_node=Doublynode(val,prev=tail)
    tail.next=new_node
    return head,new_node



def doublylinkedlist_main():
    head=tail=Doublynode(1)
    head,tail=insert_at_begining(head,tail,0)
    head,tail=insert_at_end(head,tail,2)
    display_dl(head)



if __name__=="__main__":
    doublylinkedlist_main()
    