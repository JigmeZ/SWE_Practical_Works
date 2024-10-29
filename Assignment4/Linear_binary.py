def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")


import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")



def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)


##
# Test the Linear search all indices
def linear_search_all_indices(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)  
    return indices if indices else -1  

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search_all_indices(test_list, 5)
print(f"Linear for All Indices : Indices of 5 are {result}")


def find_insertion_point(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left  # The insertion point

# Test the function
sorted_list = [1, 3, 4, 6, 8, 9]
target = 5
insertion_point = find_insertion_point(sorted_list, target)
print(f"Insertion Point for {target} is at index {insertion_point}")
print("Updated list:", sorted_list)


# Linear Search with Comparison Count
def linear_search(arr, target):
    comparisons = 0
    for i, num in enumerate(arr):
        comparisons += 1
        if num == target:
            return i, comparisons
    return -1, comparisons

# Binary Search (Iterative) with Comparison Count
def binary_search(arr, target):
    left, right, comparisons = 0, len(arr) - 1, 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

# Binary Search (Recursive) with Comparison Count
def binary_search_recursive(arr, target, left, right, comparisons=0):
    if left > right:
        return -1, comparisons
    mid = (left + right) // 2
    comparisons += 1
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons + 1)
    return binary_search_recursive(arr, target, left, mid - 1, comparisons + 1)

def main():
    test_list, target = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 6
    sorted_list = sorted(test_list)

    for search, name in [(linear_search, "Linear Search"),
                         (lambda arr, tgt: binary_search(arr, tgt), "Binary Search (Iterative)"),
                         (lambda arr, tgt: binary_search_recursive(arr, tgt, 0, len(arr) - 1), "Binary Search (Recursive)")]:
        index, comparisons = search(test_list if "Linear" in name else sorted_list, target)
        print(f"{name}: Index of {target} is {index}, Comparisons made: {comparisons}")


# Integrate jump search into main()
def main():
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    target = 6
    sorted_list = sorted(test_list) 

    # Call jump_search with the sorted list and target
    index, comparisons = jump_search(sorted_list, target)
    print(f"Jump Search: Index of {target} is {index}, Comparisons made: {comparisons}")

def jump_search(arr, target):
    n = len(arr)
    step = int(n ** 0.5)  
    prev = 0  
    comparisons = 0  # To keep track of comparisons made

    # Jump through the array to find the potential block
    while prev < n and arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1, comparisons 

    # Linear search within the blocka
    while prev < n and arr[prev] < target:
        comparisons += 1
        prev += 1
        if prev == min(step, n):
            return -1, comparisons 

    comparisons += 1
    if prev < n and arr[prev] == target:
        return prev, comparisons  # Return index and comparison count

    return -1, comparisons  

main()

if __name__ == "__main__":
    main()





