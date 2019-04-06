# sorting

# def sorting(a): #Bubble sort
#     flag=False
#     while flag==False:
#         flag=True
#         for z in range(len(a)-1,0,-1):
#             for i in range(z):
#                 if a[i]>=a[i+1]:
#                     temp= a[i]
#                     a[i]= a[i+1]
#                     a[i + 1] = temp
#                     flag=False
# a = [5,4,3,2,1]
# sorting(a)
# print(a)


#selection sort
# def selection_sort(a):
#     for i in range(len(a) - 1, 0, -1):
#         p=0
#         for j in range( i+1):
#             if a[j] > a[p]:
#                 p = j
#         temp = a[i]
#         a[i] = a[p]
#         a[p] = temp
# a = [5,4,3,2,1,0]
# selection_sort(a)
# print(a)


# binary search
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
          if item<alist[midpoint]:
            return binarySearch(alist[:midpoint],item)
          else:
            return binarySearch(alist[midpoint+1:],item)

alist = [0, 1, 2, 8, 13, 17, 19, 32, 42,57]
print(binarySearch(alist, 57))
print(binarySearch(alist, 0))











