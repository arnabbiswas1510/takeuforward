#Great thing about this method is that no sort is needed, hence O(n),
# However this method does not work without sorting (try it on the sample data below)
#Both methods below need external storage though
def merge(intervals):
    out=[]
    #intervals.sort(key=lambda x:x[0])
    start=intervals[0][0] #start with start of 0th interval
    for i in range(1,len(intervals)):
        if intervals[i-1][1]>=intervals[i][0]: #As long as prev interval overlaps with the current one
            continue
        else:
            out.append([start,intervals[i-1][1]]) #Add merged interval
            start=intervals[i][0] #Set start to start of current inetrval
    out.append([start,intervals[i][1]]) #Dont forget to add last interval after the loop
    return out

#Remember how below method negates the use of the start interval I used above
def merge1(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i[0]): #This method requires sorting
        if out and i[0] <= out[-1][1]: #If there is an overlap
            out[-1][1] = max(out[-1][1], i[1]) #Keep updating the end of the prev interval
        else:
            out += i,
    return out


print(merge([[1,3],[8,10],[2,6],[15,18]]))