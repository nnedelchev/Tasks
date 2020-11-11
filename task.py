#!/usr/bin/python3
import sys

def duplicateZeros(arr):

    ### initialization of additional vars 
    k = 0
    arr2 = []
    
    ### loop for searching of "0" items
    for i in range(0,99):
        if ln < k:
            return
        else:
            
            ### Duplicationg the "0" item
            if arr[i] == 0:
                k = k + 1
                arr2.append(0)
                #print(arr2)

            arr2.append(arr[i])
            #print(arr2)

            k = k + 1
            
            ### Print the result and exit
            if ln == k or ln < k:
                print(arr2[0:ln])
                return

### Take the input from CLI
n = len(sys.argv[1])
arr = sys.argv[1][1:n-1]
arr = arr.split(',')

### initialization of additional vars 
ln = len(arr)

### Integer conversion
for m in range(0,ln):
    arr[m] = int(arr[m])

duplicateZeros(arr)
