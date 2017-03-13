def mergesort(list):
	if len(list) < 2:
		return list
	
	mid = int(len(list)/2)

	left = mergesort(list[:mid])
	right = mergesort(list[mid:])

	return merge(left, right)

def merge(left, right):
	result = list()
	il = 0
	ir = 0

	for ix in range(len(left) + len(right)):

		if il < len(left) and ir < len(right):
			if left[il] <= right[ir]:
				result.append(left[il])
				il += 1
			else:
				result.append(right[ir])
				ir += 1
		elif ir >= len(right):
			result.append(left[il])
			il += 1
		else:
			result.append(right[ir])
			ir += 1
	
	return result

if __name__ == "__main__":
    print(mergesort([3,2,1,4,-1,-2,0]))