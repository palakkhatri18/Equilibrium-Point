#Given an array A of n non negative numbers. The task is to find the first equilibrium point in an array. Equilibrium point in an array is an index (or position) such that the sum of all elements before that index is same as sum of elements after it.
# Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists.

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here 
        totalsum = sum(A)
        
        leftsum = 0
        for i in range(N):
            
            rightsum = totalsum-A[i]-leftsum
            # if mera more than 3 present h
            if leftsum == rightsum:
                return i+1
            #nhi h toh bdao
            leftsum = A[i]+1
        # If mera do element present h
        return -1 