#stack
# stack=[]
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# stack.append(5)
# print(stack)
# stack.pop()
# print(stack)
# print(stack)
# s="[{()}]" 
# stack=[]
# d={
#     "(":")",
#     "{":"}",
#     "[":"]"
# }
# for i in s:
#     if i in d.keys():
#         stack.append(i)
#     else:
#         if not stack:
#             print("false")
#         elif d[stack.pop()]!=i:
#             print("false")
# print(len(stack)==0)
# class Minstack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,val:int)->None:
#         curr_min=val
#         if self.stack:
#             curr_min=min(curr_min,self.stack[-1][1])
#         self.stack.append([val,curr_min])
#     def pop(self)->None:
#         self.stack.pop()
#     def top(self)->int:
#         return self.stack[-1][0]
#     def getMin(self)->int:
#         return self.stack[-1][1]
# tokens=["1","2","+","3","*","4","-"]
# l=["+","-","*","/"]
# s=[]
# for i in tokens:
#     if i not in l:
#         s.append(int(i))
#     else:
#         a=s.pop()
#         b=s.pop()
#         if i =="+":
#             s.append(b+a)
#         elif i=='-':
#             s.append(b-a)
#         elif i=="*":
#             s.append(b*a)
#         else:
#             s.append(int(b/a))
# print(s[0])
# from collections import deque
# queue=deque()
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# queue.append(5)
# print(queue)
# queue.popleft()
# print(queue[0])
