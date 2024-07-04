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

def productExceptSelf2(arr): #No extra space
    n=len(arr)
    out = [1]*n
    for i in range(1,n):
        out[i]=arr[i-1]*out[i-1]
    curr = 1
    for i in range(n-1,-1,-1):
        #out[lenArr-i-1]=out[lenArr-i-1]*arr[lenArr-i]*out[lenArr-i]
        out[i]*=curr
        curr*=arr[i]
    return out

print(productExceptSelf2([2,3,4,5]))