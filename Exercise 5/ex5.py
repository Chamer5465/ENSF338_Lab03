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
    avg_times_insertion = []
    avg_times_binary = []
    
    for i in range (5, 101, 5):
        data = [j for j in range(i)]
        random.shuffle(data)
        
        avg_times_insertion.append(timeit.timeit(lambda:insertion_sort(data.copy()), number= 100) / 100)
        avg_times_binary.append(timeit.timeit(lambda:binary_insertion_sort(data.copy(), len(data)), number= 100) / 100)
        
        print(f"The average insertion sort time for a shuffled array of {i} items is {avg_times_insertion[-1]}")
        print(f"The average binary insertion sort time for a shuffled array of {i} items is {avg_times_binary[-1]}")
        
    x = [i for i in range(5, 101, 5)]
    
    plt.figure(figsize=(20, 10))
    
    plt.subplot(1, 2, 1)
    plt.scatter(x= x, y= avg_times_insertion)
    plt.title("Average Times for Insertion Sort")
    
    plt.subplot(1, 2, 2)
    plt.scatter(x= x, y= avg_times_binary)
    plt.title("Average Times for Binary Insertion Sort")
    
    plt.show()
    plt.close()
    
        
        
    
if __name__ == '__main__':
    main()