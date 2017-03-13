def selectionsort(list):
    for jx in range(0,len(list)-1):
        min = jx
        for ix in range(jx+1,len(list)):
            if list[ix] < list[min]:
                min = ix
        if min != jx:
            temp = list[jx]
            list[jx] = list[min]
            list[min] = temp
    
    return list
if __name__ == "__main__":
    print(selectionsort([2,1,3,0,-1,-3,-2,5,6,4]))