import time


def bubbleS(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp


nlist=[23,22,44,11,33,556,3,23,54,65,7,76,3,4,54,6,67,3,35,432,4,5,3,32,6,6,9,4,4,23]
bubbleS(nlist)
print(nlist)

start_time = time.time()
print("--- %s seconds ---" % (time.clock() - start_time))
#bubble sort
def bubbsort(list_a):

    for j in range(0,len(list_a)):
        for i in range(0,len(list_a)-1):
            if list_a[i]>list_a[i+1]:
                list_a[i],list_a[i+1]=list_a[i+1],list_a[i]
#print(list_a) #this line prints every step of sorting elements

list_a=[4,8,1,3,7,9,5,17,12]
bubbsort(list_a)
print("your ordered list:\n",list_a)

start_time = time.time()
print("--- %s seconds ---" % (time.clock() - start_time))