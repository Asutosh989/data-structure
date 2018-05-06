# def max_heapify(A, i):
#     l = 2 * i
#     r = 2 * i + 1
#     if (l < len(A) and A[l] > A[i]):
#         largest = l
#     else:
#         largest = i
#     if (r < len(A) and A[r] > A[i]):
#         largest = r
#     print("largest = " + str(largest))
#     if largest != i:
#         t = A[i]
#         A[i] = A[largest]
#         A[largest] = t
#         max_heapify(A, largest)

# def build_max_heap(A):
#     for i in range(len(A)//2, 0, -1):
#         print(i)
#         max_heapify(A, i)

# def heap_sort(A):
#     build_max_heap(A)
#     fi = []
#     for i in range(len(A)-1, 0, -1):
#         t = A[0]
#         A[0] = A[i]
#         A[i] = t
#         fi.append(A.pop())
#         max_heapify(A, 0)
#     return (fi)

# B = [2,5,7,9,1,10,3]
# print(B)
# d = heap_sort(B)
# print(d)


def heapsort( A ):
    # Building a max heap
    length = len( A ) - 1
    leastParent = length // 2
    for i in range ( leastParent, -1, -1 ):
        max_heapify( A, i, length )

    # flatten heap into sorted array
    for i in range ( length, 0, -1 ):
        if A[0] > A[i]:
            swap( A, 0, i )
            max_heapify( A, 0, i - 1 )

 
def max_heapify( A, first, last ):
    largest = 2 * first + 1
    while largest <= last:
    # right child exists and is larger than left child
        if ( largest < last ) and ( A[largest] < A[largest + 1] ):
            largest += 1

        # right child is larger than parent
        if A[largest] > A[first]:
            swap( A, largest, first )
            # move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return # force exit

 
def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

arr = [8,5,3,1,9,6,0,7,4,2,5]
print(arr)
heapsort(arr)
print(arr)