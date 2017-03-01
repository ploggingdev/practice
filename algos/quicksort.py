
def quicksort(to_sort, lo, hi):
    if lo < hi:
        p = partition(to_sort, lo, hi)
        quicksort(to_sort, lo, p)
        quicksort(to_sort, p + 1, hi)

def partition(to_sort, lo, hi):
    pivot = to_sort[lo]
    i = lo - 1
    j = hi + 1
    while True:
        
        i = i + 1
        while to_sort[i] < pivot:
            i = i + 1

        j = j - 1
        while to_sort[j] > pivot:
            j = j - 1

        if i >= j:
            return j
        
        temp = to_sort[i]
        to_sort[i] = to_sort[j]
        to_sort[j] = temp
    
if __name__ == "__main__":
    to_sort = [1,3,2,0,-1,4,5,1,-2,-3,1,7]
    (quicksort(to_sort, 0 ,len(to_sort)-1))
    print(to_sort)