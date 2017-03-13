def insertionsort(list):
    for ix in range(1, len(list)):
        jx = ix
        while jx > 0 and list[jx-1] > list[jx]:
            temp = list[jx]
            list[jx] = list[jx-1]
            list[jx-1] = temp
            jx -= 1
    return list

if __name__ == "__main__":
    print(insertionsort([2,1,3,0,-1,-3,-2,5,6,4]))