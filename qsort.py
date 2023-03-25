def getPivot(arr, l, r):
	return arr[r]

def partition(arr, l, r):
	p = getPivot(arr, l, r)
	i = l - 1
	for j in range(l, r):
		if arr[j] <= p:
			i += 1
			arr[j], arr[i] = arr[i], arr[j]
	arr[i+1], arr[r] = arr[r], arr[i+1]
	return i + 1


def quickSort(arr, l, r):
	if l < r:
		p = partition(arr, l, r)
		quickSort(arr, l, p - 1)
		quickSort(arr, p+1, r)


arr = [4, 3, 1, 2, 6, 5]
quickSort(arr, 0, len(arr)-1)
print(arr)
