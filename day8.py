# arr=[3,4,2,1]
# def merge_sort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         left=arr[:mid]
#         right=arr[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         lp=0
#         rp=0
#         fp=0
#         while lp<len(left) and rp<len(right):
#             if left[lp]<right[rp]:
#                 arr[fp]=left[lp]
#                 lp+=1
#                 fp+=1
#             else:
#                 arr[fp]=right[rp]
#                 rp+=1
#                 fp+=1
#         while lp<len(left):
#             arr[fp]=left[lp]
#             fp+=1
#             lp+=1
#         while rp<len(left):
#             arr[fp]=right[rp]
#             fp+=1
#             rp+=1
# print(arr)
# merge_sort(arr)
# print(arr)
# import random
# choice=['stone','paper',"scissor"]
# player=input("enter your choice stone or paper or scissor")
# computer=random.choice(choice)
# print("player choice:",player)
# print("computer choice:",computer)
# if player==computer:
#     print("tie")
# elif (player=='stone') and (computer=='scissor'):
#     print("player win")
# elif (player=='paper') and(computer=='stone'):
#     print("player win")
# elif (player=='scissor') and(computer=='paper'):
#     print("player win")
# else:
#     print("computer win")
# import random
# arr=[3,4,2,1]
# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr
#     else:
#         pivot=random.choice(arr)
#         left=[]
#         right=[]
#         middle=[]
#         for i in arr:
#             if i<pivot:
#                 left.append(i)
#             elif i==pivot:
#                 middle.append(i)
#             else:
#                 right.append(i)
#         return quick_sort(left)+quick_sort(middle)+quick_sort(right)
# print(quick_sort(arr))
