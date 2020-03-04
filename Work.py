#  File: Work.py 

#  Description: Use binary and linear search to find the optimal method. 

#  Student Name: Jade Jaiyesimi

#  Student UT EID: jaj3847

#  Course Name: CS 313E

#  Unique Number: 50295 

#  Date Created: February 22nd, 2020

#  Date Last Modified: February 24th, 2020

import time

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int: # adapted from class notes
    p = 0
    for i in range (0,n): 
        v = find_v(i,k)
        if v >= n: 
            break
    return i
 
# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:  #adapted from class notes
    low,p = 0,0
    high = n-1
    while high >= low:
        mid = (high + low) // 2
        v = find_v(mid,k)
        if  v < n:
            low = mid + 1
        elif v > n:
            high = mid - 1
        else: 
            return mid
    return mid
        
def find_v (n,k):
    val = 0
    for i in range(n):  #find summation of lines coded (estimated n)
        val = val + n//(k**i)
        if (n//(k ** i)) == 0:
            break
    return val

# main has been completed for you
# do NOT change anything below this line
def main():
  in_file = open("work.txt", "r")
  num_cases = int((in_file.readline()).strip())

  for i in range(num_cases):
    inp = (in_file.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
