inv = 0

def merge(a, b):
	arr = []
	i = j = 0
	al = len(a)
	bl = len(b)
	global inv

	while i<al and j<bl:
		if a[i] <= b[j]:
			arr.append(a[i]) 
			i += 1
		else:
			inv += al - i
			arr.append(b[j])
			j += 1

	while i<al:
		arr.append(a[i])
		i += 1
	while j<bl:
		arr.append(b[j])
		j += 1
	return arr

def mergeSort(arr):
	n = len(arr)
	if n > 1:
		a = mergeSort(arr[:n//2])
		b = mergeSort(arr[n//2:n])
		c = merge(a, b)
		return c
	return arr

# arr = [6, 5, 4, 3, 2, 1]
# mergeSort(arr)
# print(inv)

with open('int.txt', 'r') as file:
	content = file.read().split('\n')[:-1]
	num = list(map(int, content))
	mergeSort(num)
	print(inv)
