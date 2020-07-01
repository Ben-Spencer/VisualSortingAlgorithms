#Selection Sort

def selectionSort(arr):
    for i in range(len(arr)): 
        key = i 
        for j in range(i+1, len(arr)): 
            if arr[key] > arr[j]: 
                key = j 
        arr[i], arr[key] = arr[key], arr[i] 
    return arr

arr = [64, 25, 12, 22, 11] 
print(selectionSort(arr))
