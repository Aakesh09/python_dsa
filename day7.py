# arr=[10,20,30,40,50,4,54]
# target=int(input("enter a value"))
# for i in range(len(arr)):
#     if arr[i]==target:
#         print(i)
# arr=[5,7,12,17,23,36,47,54]
# target=47
# left,right=0,len(arr)-1
# while left<=right:
#     middle=(left+right)//2
#     if arr[middle]==target:
#         print(arr[middle])
#         break
#     elif arr[middle]<target:
#         left=middle+1
#     elif arr[middle]>target:
#         right=middle-1
#     else:
#         print("not found")
# arr=[1,2,3,4,4,4,6,6,7]
# target=4
# left,right=0,len(arr)-1
# while left<=right:
#     middle=(left+right)//2
#     if arr[middle]==target:
#         ans=middle
#         left=middle+1
#     elif arr[middle]<target:
#         left=middle+1
#     else:
#         right=middle-1
# print(ans)
# arr=[1,2,3,4,4,4,6,6,7]
# target=4
# left,right=0,len(arr)-1
# while left<=right:
#     middle=(left+right)//2
#     if arr[middle]==target:
#         ans=middle
#         right=middle-1
#     elif arr[middle]<target:
#         left=middle+1
#     else:
#         right=middle-1
# print(ans)
# left=0
# right=144
# target=145
# while left<=right:
#     mid=(left+right)//2
#     if mid*mid==target:
#         print(mid)
#         break
#     elif mid*mid<target:
#         ans=mid
#         left=mid+1
#     else:
#         right=mid-1        
# print(mid)
# arr=[2,5,1,9,3,4,6,8,7]
# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(len(arr)-1):
#         for j in range(i,len(arr)-1):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#     return arr
# print(bubble_sort(arr))
arr=[2,5,1,9,3,4,6,8,7]
def Selection_arr(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
print(Selection_arr(arr))