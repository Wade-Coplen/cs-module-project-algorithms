'''
Input: a List of integers
Returns: a List of integers
---------------------------
Understanding the Problem
- Takes in an array as a parameter
- returns a new array?
- in place?
- find the product of all the numbers in the array
- EXCEPT at the a specified index. 
- import combinations?
- What do they mean by THAT index
- Is THAT index an parameter?
- Do we make it up?
- is it always index zero?

'''
def product_of_all_other_numbers(arr):
    # Your code here
    
    
    for num in arr:
        start = arr[num] +1
        result = start * num
    return result

       
        
        


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
