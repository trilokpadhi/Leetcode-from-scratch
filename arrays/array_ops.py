# Operations on arrays
# There are 4 types of operations

# 1. insertEnd - insert n into array arr at the end if arr is not full
# 2. removeEnd - remove from the last position in the array and if arr is not empty
# 3. insertStart - insert n into array arr at the start if arr is not full
# 4. removeStart - remove from the first position in the array and if arr is not empty
# 5. insertMiddle - insert n into index i after shifting elements to the right
# 6. removeMiddle - remove value at index i before shifting elements to the left
# 7. getValue - get the value at index i if arr is not empty  (optional)


# Length is the number of 'real' values in arr, 
# Capacity is the size (aka memory allocated for the fixed size array).

class ArrayOps:
    def __init__(self, arr, length, capacity):
        self.arr = arr
        self.length = length
        self.capacity = capacity
    def insertEnd(self, n):
        """ 
        Insert n into array arr at the end if arr is not full.
        Args:
            arr: array ( the array to be inserted into )
            n: number ( the number to be inserted )
            length: number ( the length of the array )
            capacity: number   ( the capacity of the array )
        """
        if self.length < self.capacity:
            # self.arr[self.length] = n
            self.arr.append(n)
            self.length += 1


    def removeEnd(self):
        """ 
        Remove from the last position in the array and if arr is not empty
        Args:
            arr: array ( the array whose last element is to be removed)
            length: number ( the length of the array )
        """
        if self.length > 0:
            # Overwrite last element with some default value.
            # We would also the length to decreased by 1.
            self.arr[self.length - 1] = 0
            self.length -= 1

    def insertStart(self, n):
        """
        Insert n into array arr at the start if arr is not full.
        Args:
            arr ([typing.List]): [the array to be inserted into]
            n ([int]): [the number to be inserted]
            length ([int]): [the length of the array]
            capacity ([int]): [the capacity of the array]
        """
        
        if self.length < self.capacity and self.length >= 0:
            # # Method 1: Append an element at the end, then shift elements to the right
            # self.arr.append(n)
            # self.length += 1
            # for index in range(self.length, 0, -1):
            #     self.arr[index] = self.arr[index - 1]
            # self.arr[0] = n  
            
            # Method 2: Insert at index 0 - more pythonic and efficient
            self.arr.insert(0, n) 
            self.length += 1  
            
        #  now insert n at index 0
        # self.arr[0] = n
        return self.length

    def removeMiddle(self, i):
        """
        Remove value at index i before shifting elements to the left.
        Args:
            arr ([typing.List]): [the array whose last element is to be removed]
            i ([int]): [the index of the element to be removed]
            length ([int]): [the length of the array]
        """
        # Shift starting from i + 1 to end.
        for index in range(i + 1, self.length):
            self.arr[index - 1] = self.arr[index]
        # No need to 'remove' arr[i], since we already shifted
        
    def printArr(self):
        print(self.arr)
        # for i in range(self.capacity):
            # print(self.arr[i])
            

arr = [1,2,3,4,5]
length = 5
capacity = 8
a = ArrayOps(arr, length, capacity)
a.printArr()
a.insertEnd(6)
a.printArr()
a.removeEnd()
a.printArr()
a.insertStart(0)
a.printArr()
a.removeMiddle(2)
a.printArr()


