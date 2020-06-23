def insertionSort(arr):
	for i in range(0,len(arr)):
		key = arr[i]
		j = i-1
		while j >=0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
			arr[j+1] = key
	return arr

arr = [5,8,5,7,3,2,1,5,6]
print(insertionSort(arr))
