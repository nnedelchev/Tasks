#!/usr/bin/python3
import sys

def duplicateZeros(arr):

    k = 0
    arr2 = []

    for i in range(0,99):
        if ln < k:
            return
        else:

            if arr[i] == 0:
                k = k + 1
                arr2.append(0)
                #print(arr2)

            arr2.append(arr[i])
            #print(arr2)

            k = k + 1
            if ln == k or ln < k:
                print(arr2[0:ln])
                return


n = len(sys.argv[1])
arr = sys.argv[1][1:n-1]
arr = arr.split(',')
ln = len(arr)

for m in range(0,ln):
    arr[m] = int(arr[m])

duplicateZeros(arr)
