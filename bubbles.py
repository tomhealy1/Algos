import timeit
start = timeit.default_timer()

# All the program statements

def bubbleS(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp


nlist=[2,45,3,22,56,88,1212,34,9696,3,5,34,5,3,65,34,54,1,0]
bubbleS(nlist)
print(nlist)

       
stop = timeit.default_timer()
execution_time = stop - start

print(('{:.9f}'.format(execution_time))) # It returns time in seconds to 9 decimal places
