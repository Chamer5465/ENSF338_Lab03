import random
import timeit
from matplotlib import pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def binary_search(a, item, low, high):
    while (low <= high):
        mid = low + (high - low) // 2
        if (item == a[mid]):
            return mid + 1
        elif (item > a[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return low

def binary_insertion_sort(a, n):
    for i in range (n): 
        j = i - 1
        selected = a[i]
         
        loc = binary_search(a, selected, 0, j)
         
        while (j >= loc):
            a[j + 1] = a[j]
            j-=1
        a[j + 1] = selected
        
def main():
    num_trials = 10  
    avg_times_insertion = []
    avg_times_binary = []
    
    for i in range(10, 1501, 10): 
        insertion_times = []
        binary_times = []
        
        for _ in range(num_trials):
            data = [j for j in range(i)]
            random.shuffle(data)  
            
            insertion_times.append(timeit.timeit(lambda: insertion_sort(data.copy()), number=1))
            binary_times.append(timeit.timeit(lambda: binary_insertion_sort(data.copy(), len(data)), number=1))
        
        avg_times_insertion.append(sum(insertion_times) / num_trials)
        avg_times_binary.append(sum(binary_times) / num_trials)
        
        print(f"Size {i}: Insertion Sort Avg Time = {avg_times_insertion[-1]:.6f}, Binary Insertion Sort Avg Time = {avg_times_binary[-1]:.6f}")
        
    x = [i for i in range(5, 1501, 10)]
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(x, avg_times_insertion, label="Insertion Sort", marker='o')
    plt.plot(x, avg_times_binary, label="Binary Insertion Sort", marker='s')
    
    plt.xlabel("Array Size")
    plt.ylabel("Average Time")
    plt.title("Insertion Sort vs. Binary Insertion")
    plt.legend()
    plt.grid()
    
    plt.show()
    
if __name__ == '__main__':
    main()




'''
Q4)
Search complexity
Insertion sort complexity (O(n))
Binary insertion sort complexity(O(log n))

Shifting complexity
Insertion sort complexity (O(n))
Binary insertion sort complexity(O(n))

The resources to shift are much higher than the resources to search so even if the search is of lower complexity the overall time is very similar with the binary insertion sort being very slightly faster.
'''