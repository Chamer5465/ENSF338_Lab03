import matplotlib.pyplot as plt
import timeit
import numpy as np


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# this is taken from lecture 12
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr,low,high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
        
def main():
    # Quick sort has a complexity of o(n*n) when
    # the chosen pivot is either the highest or lowest
    # value. This happens when the array is already sorted
    # or reversed sorted
    array_sizes = [16, 32, 64, 128, 256, 512]
    times = []
    
    for size in array_sizes:
        arr = list(range(size))
        time_elapsed = timeit.timeit(lambda: quick_sort(arr.copy(), 0, len(arr) - 1), number=10)
        times.append(time_elapsed)
        
    print(times)
    
    plt.plot(array_sizes, times, 'o-', label='Measured Execution Time')
    plt.plot(array_sizes, np.array(array_sizes) ** 2 / max(array_sizes) ** 2 * max(times), 
             '--', label='O(n^2) Reference')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (sec)")
    plt.title("Quicksort Worst-Case Complexity")
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()
    
