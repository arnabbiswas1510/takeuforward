"""
Note here is that regular prefix array is calculated as follows:
* Iterate over the given array from indices 1 to N – 1.
* Calculate arr[i] = arr[i] * arr[i-1] for every ith index. #This is wrong, see below
But since we want to exclude self, note how we do it below instead

The intuition for the product of an array except the current element is to calculate the product of all numbers to the
left of the current element and multiply it by the product of all numbers to the right.
Here are the steps to calculate the product of an array except the current element:
Initialize two variables, left and right, to 1.
Create an array ans to store the results.
Traverse the array from left to right.
For each ans[i], multiply it by the current product on its left.
Update left to include nums[i].
Traverse the array from right to left.
For each ans[i], multiply it by the current product on its right.
Update right to include nums[i].
At the end of these two passes, each ans[i] will contain the product of all other numbers except for nums[i]
"""
def productExceptSelf(arr):
    lenArr=len(arr)
    prefix = [1]*lenArr
    postfix = [1]*lenArr
    out = [1]*lenArr
    for i in range(1,lenArr):
        prefix[i]=arr[i-1]*prefix[i-1]
    for i in range(1,lenArr):
        postfix[lenArr-i-1]=arr[lenArr-i]*postfix[lenArr-i]
    for i in range(0,lenArr):
        out[i]=prefix[i]*postfix[i]
    return out

#Need only one out array here and one less loop
def productExceptSelf2(arr): #No extra space
    n=len(arr)
    out = [1]*n
    for i in range(1,n):
        out[i]=arr[i-1]*out[i-1]
    right=1 #Use this variable here
    for i in range(n-1,-1,-1):
        out[i]*=right
        right*=arr[i] #Remember the multiplication here
    return out

print(productExceptSelf2([2,3,4,5]))