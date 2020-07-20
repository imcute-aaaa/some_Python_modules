def ms(a):
    print('splt',a)
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        ms(left)
        ms(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k+=1
        while i < len(left):
            a[k]=left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        print('merg',a)           
hh=[]
import random
def cms(ln,mn=0,mx=100):
    for i in range(ln):
        hh.append(random.randint(mn,mx))
cms(995,1000000000000000000000000000000000000000000000000,1000000000000000000000000000000000000000000000010)
ms(hh)
