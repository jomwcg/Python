def median(n):
    sort = sorted(n)
    if len(n) % 2 == 0:
        a = len(sort) / 2
        b = a + 1
        return (sort[len(sort) / 2 - 1] + sort[len(sort) / 2]) / 2.0
    else:
        return sort[len(sort) / 2]
    #return sort

print median([1,3,2,5,4,6,7])