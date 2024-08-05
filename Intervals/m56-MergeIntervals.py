def merge(intervals):
    out=[]
    start=intervals[0][0]
    for i in range(1,len(intervals)):
        if intervals[i-1][1]>=intervals[i][0]:
            continue
        else:
            out.append([start,intervals[i-1][1]])
            start=intervals[i][0]
    out.append([start,intervals[i][1]])
    return out

#Remember how below method negates the use of the start interval I used above
def merge1(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i[0]):
        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], i[1])
        else:
            out += i,
    return out

print(merge([[1,3],[2,6],[8,10],[15,18]]))