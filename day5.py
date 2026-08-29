# arr=[2,5,4,6,7,9]
# sum=0
# for i in range(len(arr)):
#     sum +=arr[i]
# print(sum)
# arr=[2,5,4,6,7,9]
# sum=0
# for i in range(2,6):
    # sum +=arr[i]
    # if i>=2 and 5:
    #     sum +=arr[i]
# print(sum)
# def build_prefix(arr):
#     prefix=[]
#     sum=0
#     for i in arr:
#         sum +=i
#         prefix.append(sum)
#     return prefix
# def prefix_sum(prefix,start,end):
#     if start==0:
#         return prefix[end]
#     return prefix[end]-prefix[start]-1    
# arr=[2,3,4,5,6,7,8,9]
# print(build_prefix(arr))
# prefix=build_prefix(arr)
# print(prefix_sum(prefix,2,6))
# def equillibrium_sum(arr1):
#     total=sum(arr1)
#     left_sum=0
#     for i in range(len(arr1)):
#         right_sum=total-arr1[i]-left_sum
#         if right_sum==left_sum:
#             return [arr1[i],i]
#         left_sum+=arr1[i]
#     return -1
# arr1=[-7,1,5,2,-4,3,0]
# print(equillibrium_sum(arr1))
          

    