# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def add_node(self,data):
#         node=Node(data)
#         if not self.head:
#             self.head=node
#         else:
#             current=self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=node
#         def delete(self,data):
#             if self.head.data==data:
#                 self.head=self.head.next
#             else:
#                 current=self.head
#                 while current.next is not None:
#                     if current.next.data==data:
#                         current.next=current.next.next
#                         print("deleted")
#                         return
#                     current=current.next
#                     print("not found")
#         def display(self):
#             current=self.head
#             while current is not None:
#                 print(current.data,"->",end=" ")
#                 current=current.next
#             print("None")
#         def insert_at_beginning(self,data):
#             node=Node(data)
#             if not self.head:
#                 self.head=node
#             else:
#                 node.next=self.head
#                 self.head=node
#         def insert_at_Kth_position(self,data,k):
#             node=Node(data)
#             if not self.head:
#                 self.head=node
#             else:
#                 current=self.head
#                 count=1
#                 while current is not None  and k >1:
#                     current=current.next
#                     count+=1
#                     if count ==k-1:
#                         node.next=current.next
#                         current.next=node
#                         print("inserted at kth position")
#                         return
#                 print('not found')
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Double_linked_list:
    def __init__(self):
        self.head=None
    def add_node(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
                
            current.next=node