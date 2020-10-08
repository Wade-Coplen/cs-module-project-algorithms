'''
Input: a List of integers
Returns: a List of integers
--------------------------
Understanding the Problem:
Could be positive or negative integer
It says the LEFT side of the array, which infers there is a RIGHT side, which
means there is a MIDDLE

LEFT - anything that is NOT ZERO, which is anything but zero
MIDDLE --> start + end // 2
RIGHT - has to be 0

Possibly a binary searching left -1 and right -1

'''
def moving_zeroes(arr):
    # Find the middle
    # iterate over the list and divide length by floor 2
    # have to find a middle
    for i in range(0, len(arr) -1):
        middle = (len(arr) -1) // 2
        #print(middle)
     
        if arr[middle] == 0:
            return arr[middle + 1]

    # Your code here

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")