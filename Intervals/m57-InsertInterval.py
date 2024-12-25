"""
Just memorize given algo below
"""
def insert(intervals, interval):
    out=[]
    for i in range(len(intervals)):
        #Remember below flow
        if intervals[i][0] > interval[1]: #If interval lies before current interval
            out.append(interval) #Append interval
            out.append(intervals[i:]) #Append all remaining intervals. Why is break redundant here? It's not!!
            break
        elif(intervals[i][1] < interval[0]): #If interval lies after current interval
            out.append(intervals[i]) #Remember this and not inserting actual interval here
        else: #If there is an overlap
            interval=[min(interval[0], intervals[i][0]), #Modify interval and make it the largest one,
                      # but dont append to out
                      max(interval[1], intervals[i][1])]
    return out

# print(insert([[1,3],[6,9]],[2,5]))
print(insert([[1,2], [3,5], [6,7], [8,10], [12,16], [17,18]],[4,9]))