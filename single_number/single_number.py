'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
U- 
    a list where every integer (i) shows up twice except one (j)
    example = [1, 1, 2, 2, 4, 4, 3, 3, 5]
               ^  ^
            i[0] i[1]
# is this list sorted?
# what if it is unsorted?
# We are going to have to 
# we need to look at each index. Then compare that index to the previous index and next index..i[0] <--> i[1]<--> i[2]
# if no previous to compare, move to next index. 
# if current_index is == previous_index or current_index is == next_index, it is not the single integer we are looking for. Next
# if current_index is != prev_index nor is it equal to the next_index, return current_index
# so this list CANNOT be sorted as it runs of a random number generator. Each run has a new set of numbers. 
'''
def single_number(arr):
    # Your code here
    sorted_array = list(sorted(arr))
    print(sorted_array)
    for i in len(sorted_array) - 1:
        current_index = sorted_array[i]
        next_index = current_index + 1
        previous_index = current_index - 1
        if current_index -1 == current_index or current_index == next_index:
            return None
        if current_index == next_index or previous_index:
            return current_index
        else:
            if i != next_index or previous_index:
               return current_index



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")