import timeit
start = timeit.default_timer()

# All the program statements
def inSort(nlist):
   for i in range(1,len(nlist)):

     currentvalue = nlist[i]
     pos = i
#move all elements > currentvalue (key) right by 1 position
     while pos>0 and nlist[pos-1]>currentvalue:
         nlist[pos]=nlist[pos-1]
         pos = pos-1

     nlist[pos]=currentvalue

nlist = [2,45,3,22,56,88,1212,34,9696,3,5,34,5,3,65,34,54,1,0]
inSort(nlist)
print(nlist)

       
stop = timeit.default_timer()
execution_time = stop - start

print(('{:.9f}'.format(execution_time))) # It returns time in seconds to 9 decimal places