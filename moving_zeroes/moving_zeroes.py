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

1. Find the middle
[0, 3, 1, 0, -2]
       ^
        middle = (len(arr) -1) // 2
2. Split up into 3 lists
    a. [0, 3]
    b. [1]
    c. [0, 2]
-or-
 iterate through the list. if anything is bigger than 0, append
 to its own list. 
 3. Should have two lists. [0,0] and [3, 1, 2]
 4. join two lists
'''
def moving_zeroes(arr):
    # Find the middle
    # iterate over the list and divide length by floor 2
    # have to find a middle
    before = []
    middle_index = (len(arr) -1) // 2
    #print(middle_index)
    middle = []
    after = []
    for i in arr:
        #print(i)
        if i == 0:
            middle.append(i)
            #print(middle)
        elif i is not 0:
            before.append(i)
           # print(before)
    for x in before:
        middle.append(x)
    print(middle)
            

    # Your code here




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")