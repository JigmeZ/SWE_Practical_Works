def in_place_quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        in_place_quick_sort(arr, low, pivot_index - 1)
        in_place_quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1 
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the element at i + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
in_place_quick_sort(test_arr, 0, len(test_arr) - 1)
print("In-Place Quick Sort Result:", test_arr)



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Modified Bubble Sort Result:", sorted_arr)




# Threshold for switching to Insertion Sort
THRESHOLD = 10

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_merge_sort(arr, left, right):
    if right - left <= THRESHOLD:
        insertion_sort(arr, left, right)
    else:
        if left < right:
            mid = (left + right) // 2
            hybrid_merge_sort(arr, left, mid)
            hybrid_merge_sort(arr, mid + 1, right)
            merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    left_sub = arr[left:mid + 1]
    right_sub = arr[mid + 1:right + 1]
    
    i, j = 0, 0
    k = left
    
    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] <= right_sub[j]:
            arr[k] = left_sub[i]
            i += 1
        else:
            arr[k] = right_sub[j]
            j += 1
        k += 1
    
    while i < len(left_sub):
        arr[k] = left_sub[i]
        i += 1
        k += 1
    
    while j < len(right_sub):
        arr[k] = right_sub[j]
        j += 1
        k += 1

# Test the hybrid Merge Sort function
test_arr = [64, 34, 25, 12, 22, 11, 90, 3, 17, 10, 2]
hybrid_merge_sort(test_arr, 0, len(test_arr) - 1)
print("Hybrid Merge Sort Result:", test_arr)




import time

# Helper function to print the array
def print_array(arr):
    print(" ".join(f"{x:2}" for x in arr))
    time.sleep(0.2)

# Bubble Sort with visualization
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print_array(arr)
    return arr

# Merge Sort with visualization
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            print_array(arr)

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            print_array(arr)

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            print_array(arr)

# Quick Sort with visualization
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print_array(arr)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print_array(arr)
    return i + 1
# refrence from chat gpt

# Test the sorting functions
arr = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort:")
bubble_sort(arr.copy())
print("\nMerge Sort:")
merge_sort(arr.copy())
print("\nQuick Sort:")
quick_sort(arr.copy(), 0, len(arr) - 1)


