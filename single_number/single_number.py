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
# We are going to have to do if we cannot sort the list. iterate and pop and append?
# if sorted, we need to look at each the first index. Then compare that index to the previous index and next index..i[0] <--> i[1]<--> i[2]
# if no previous to compare, move to next index. 
# if current_index is == previous_index or current_index is == next_index, it is not the single integer we are looking for. Next
# if current_index is != prev_index nor is it equal to the next_index, return current_index
# range(0, len(a), 2)
'''
def single_number(arr):
    # Your code here
    sorted_list = list(sorted(arr))
    #print(sorted_list)
    new_list = []
    for i in range(0, len(sorted_list) - 1):
        for j in sorted_list:
            if sorted_list[i] == sorted_list[j]:
                continue
            else:
                new_list.append(j)
    print(new_list)
       
   
            
           
    
        
        
    

    

        




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")