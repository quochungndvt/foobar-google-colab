def solution(xs):
    #code here
    if len(xs) <=2 and 0 in xs:
        return max(xs)
    #print "xs", xs
    r = 1
    largest_negative = float("-inf")
    for i in xs:
        r = max(r, r*i, key=abs)
        #print "r", r
        if i<= -1:
            largest_negative = max(i, largest_negative)
            #print "largest_negative", largest_negative
    #print "max", max(r, r // largest_negative)
    return max(r, r // largest_negative)