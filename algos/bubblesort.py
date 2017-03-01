
def bubblesort(to_sort):
    list_len = len(to_sort)
    while list_len>0:
        new_n = 0
        for ix in range(1,list_len): #checks till n-1
            if to_sort[ix-1] > to_sort[ix]:
                temp = to_sort[ix-1]
                to_sort[ix-1] = to_sort[ix]
                to_sort[ix] = temp
                new_n = ix
        list_len = new_n
    return to_sort
    
if __name__ == "__main__":
    to_sort = [1,3,2,0,-1,4,5]
    print(bubblesort(to_sort))