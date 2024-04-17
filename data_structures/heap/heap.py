# What is a heap?
# A heap is a complete binary tree that satisfies the heap property. There are two types of heaps: max and min. 
# The heap property states that the key of a node is greater than or equal to the keys of its children. This is called a max heap. 
# A min heap is a complete binary tree that satisfies the heap property where the key of a node is less than or equal to the keys of its children.
# Max heap is used for Heap sort
# Min heap is used for priority queue

# How do we built heap from an unordered list?

def max_heapify(arr, heap_size, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, heap_size, largest)
        