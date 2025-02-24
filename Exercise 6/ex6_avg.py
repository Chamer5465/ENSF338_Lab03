import timeit
import random
from matplotlib import pyplot as plt
import sys

sys.setrecursionlimit(200000)

input_sizes = [10, 20, 50, 100, 200, 500, 1000]

def binarySearch(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)
    else:
        return -1

def linear_search(arr, N, x):
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1

def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index)
        quick_sort(array, pivot_index + 1, high)

def partition(array, low, high):
    pivot = array[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and array[left] <= pivot:
            left += 1
        while array[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            array[left], array[right] = array[right], array[left]
        array[low], array[right] = array[right], array[low]
        
        return right

def sort_n_search(array, low, high, x):
    quick_sort(array, low, high)
    binarySearch(array, 0, len(array) - 1, x)
    
    
def main():
    avg_times_linear = []
    avg_times_binary = []
    worst_times_binary = []
    
    for size in input_sizes:
        data = [x for x in range(size)]
        lin_rez = []
        bin_rez = []
        
        for i in range(100):
            random.shuffle(data)
            lin_rez.append(timeit.timeit(lambda:linear_search(data, len(data), 10), number= 100) / 100)
            bin_rez.append(timeit.timeit(lambda:sort_n_search(data, len(data) // 2, len(data) // 2 + 1, 10), number= 100) / 100)
        
        avg_times_linear.append(sum(lin_rez) / len(lin_rez))
        avg_times_binary.append(sum(bin_rez) / len(bin_rez))
        
    plt.figure(figsize=(30, 10))
    
    plt.plot(input_sizes, avg_times_linear, label= 'Linear search')
    plt.plot(input_sizes, avg_times_binary, label= 'Binary search')
    
    plt.title("Performance Analysis of Binary Search and Linear Search")
    plt.legend(loc="upper left")
    plt.xlabel("Input sizes")
    plt.ylabel("Average times")

    plt.show()
        
#For inputs of smaller than about 70 elements, linear search is faster than sorting and using binary search, but for inputs of larger than 70 elements, sorting and then using binary search is significantly faster.
        

if __name__ == '__main__':
    main()