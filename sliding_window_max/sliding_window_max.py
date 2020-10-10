'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
-----------------------------
Understanding the Problem:
- Given a list of any size of integers, and a window size of (x). Determine
the largest value in each window. 
- Window size is the total number of positions the window will cover in
the existing/given list
    Example: k = 3, where k covers three of the possible indexes in a list
- Remove from current list
- Add to new list
- Traverse the list, left to right according to the size of the window
    Example:
        Window 1: index 0 1 2 --> OUTPUT MAX VALUE
        Window 2: index 1 2 3
        Window 3: index 2 3 4
        Window 4: index 3 4 5
        Window 5: index 4 5 6
- With each loop we need to move the front and end of the window forward one
index.
- K ==> could be any number. If it were static I could set it as an integer and then compare. 
- But since it isnt I need to account for less than and greater than. 

))))))))))))))
- okay so divide the nums by k 
- that will determine the number of windows. 
- Which will in turn determine the total # of max values. 
 Example:
    15 integers and we move at a 3 integer window, we should have 5 max values
    K represents the SIZE of the window
    Return a list of all integers 

    [[1, 2, 4], 4, 5, 7, 8]
         ^
    this is a sublist
How do we find the max() of a sublist regardless of size?
    K
[1, 2, 4], 4, 5, 7, 8]
    ^
for k in nums:
'''
def sliding_window_max(nums, k):
    # Your code here
  
    for k in nums:
        for i in nums:
            return max(nums)
          
      # we want to extract the largest integer from that sublist
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
