def threeSum(arr):
    res=[]
    for i in range(len(arr)):
        s = set() #Note where you initialize s
        for j in range(i+1, len(arr)):
            if -(arr[i]+arr[j]) in s:
                #You make results unique by declaring res as a set instead
                res.append((arr[i], arr[j], -(arr[i]+arr[j])))
            else:
                s.add(arr[j]) #Note what you add to s
    return res

#This problem asks for the numbers themselves to be returned (ano not indexes). Hence below method will work (we lose
# indexes after sorting)
def threeSum2(arr):
    res=[]
    arr.sort() #This is fundamental to this method
    for i in range(len(arr)): #No set needed here, obviously
        j=i+1
        k=len(arr)-1
        while j < k:
            sum = arr[i] + arr[j] + arr[k] #Do this, makes it easier
            if sum > 0:
                k-=1
            elif sum < 0:
                j+=1
            else: #Found answer
                res.append((arr[i], arr[j], arr[k]))
                #Remember to do the below here
                k-=1
                j+=1
                #Doing the below eliminates duplicates
                #But why do it at this indentation??
                while arr[j-1] == arr[j]:
                    j+=1
                while arr[k] == arr[k+1]: #Why k+1?
                    k-=1
    return res

print(threeSum2([-1,0,1,2,-1,-4]))
