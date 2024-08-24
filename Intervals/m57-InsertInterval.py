def insert(intervals, interval):
    out=[]
    for i in range(len(intervals)):
        #Remember below flow
        if intervals[i][0] > interval[1]: #If interval lies before current interval
            out.append(interval) #Append interval
            out.append(intervals[i:]) #Append all remaining intervals. Why is break redundant here?
        elif(intervals[i][1] < interval[0]): #If interval lies after current interval
            out.append(intervals[i]) #Remember this and not inserting actual interval here
        else: #If there is an overlap
            interval=[min(interval[0], intervals[i][0]), #Modify interval and make it the largest one
                      max(interval[1], intervals[i][1])]
    return out

print(insert([[1,3],[6,9]],[2,5]))