# n=5
# for i in range(n):
#     for j in range(n):
#         print('*',end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n,i,-1):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(i,end="")
#     print()
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("x",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for  j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("x",end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# n=10
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1 or j==i or n-i-1==j:
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
#     print()
# n=int(input("enter a number:"))
# total=0
# temp=n
# power=len(str(n))
# while temp>0:
#     i=temp%10
#     total=total +(i**power)
#     temp=temp//10
# if n==total:
#     print("armstrong")
# else:
#     print("not armstrong")
# n=int(input("enter a number:"))
# count=0
# for i in range(1,n):
#     if n%i==0:
#         count +=i
#         print(i)
# print(count==n)
# n=int(input("enter a number:"))
# temp=n
# sum=0
# while temp>0:
#     digit=temp%10
#     for i in range(1,digit+1):
#         fact=1
#         fact=fact*i
#         sum=sum+fact
#     temp/=10
# print(sum)
# def fun(n):
#     if n <= 1:
#         return 1
#     return n*fun(n-1)
# n=int(input("enter a number:"))
# print(fun(n))
