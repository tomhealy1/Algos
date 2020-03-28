import timeit
start = timeit.default_timer()

# All the program statements
stop = timeit.default_timer()
execution_time = stop - start

def selSort(nlist):
    for slot in range(len(nlist)-1,0,-1):
        maxpos=0
        for location in range(1, slot+1):
            if nlist[location]>nlist[maxpos]:
                maxpos= location

        temp = nlist[slot]
        nlist[slot] = nlist[maxpos]
        nlist[maxpos] = temp

nlist = [2,45,3,22,56,88,1212,34,9696,3,5,34,5,3,65,34,54,1,0]
selSort(nlist)
print(nlist)


print(('{:.9f}'.format(execution_time))) # It returns time in seconds to 9 decimal places