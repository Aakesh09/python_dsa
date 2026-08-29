# arr=[3,4,5,6]
# target=9
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)-1):
#         if target==arr[i]+arr[j]:
#             print([arr[i],arr[j]])
#             break
# arr=[3,4,5,6,7,8,9]
# target=9
# left,right=0,len(arr)-1
# while left<right:
#     if target==arr[left]+arr[right]:
#         print(arr[left],arr[right])
#         break
#     elif arr[left]+arr[right]>target:
#         right -=1
#     else:
#         left -=1
# a=(input("enter a word:"))
# left,right=0,len(a)-1
# while left<right:
#     if a[left]==a[right]:
#         left +=1
#         right -=1
#     else:
#         print("not palindrome")
# print("given word is palindrome")
# print(a[left],a[right])
# arr=[1,7,2,5,4,7,3,6]
# left,right=0,len(arr)-1
# max_area=0
# while left<right:
#     height=min(arr[left],arr[right])
#     width=right-left
#     max_area=max(max_area,height*width)
#     if arr[left]<arr[right]:
#         left +=1
#     else:
#         right -=1
# print(max_area)
# nums=[2,3,1,2,4,3]
# target=7
# left,right=0,0
# min_length=float('inf')
# curr_sum=0
# while right<len(nums):
#     curr_sum +=nums[right]
#     right +=1
#     while curr_sum>=target:
#         min_length=min(min_length,right-left)
#         curr_sum -=nums[left]
#         left+=1
# print(0 if min_length ==float('inf') else min_length)
# nums=[1,12,-5,-6,50,3]
# k=4
# left,right=0,k-1
# curr_sum=sum(nums[left:right+1])
# max_sum=curr_sum
# while right<len(nums)-1:
#     curr_sum -=nums[left]
#     left +=1
#     right +=1
#     curr_sum +=nums[right]
#     max_sum=max(max_sum,curr_sum)
# print(max_sum/k)