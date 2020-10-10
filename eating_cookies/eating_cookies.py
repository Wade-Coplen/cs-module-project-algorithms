'''
Input: an integer
Returns: an integer
------------------
Understanding the Problem:
- The solution needs to be optimized for large inputs 
- Possible ways he can eat 3 cookies:
- 1 1 1
- 1 2
- 2 1
- 3
- What if there were 10 cookies?:
- He could eat 10 cookies one at a time
    - 1 1 1 1 1 1 1 1 1 1 
- He would eat 2 cookies at a time:
    - 2 2 2 2 2 
- He could eat:
    - 1 2 3 4 at a time
    - 2 3 4 1
    - 1 3 4 2
    - etc.
- Each combo needs to have a remainder of 0
- So each combo needs to end itself

'''
def eating_cookies(n):
    # Your code here

    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
