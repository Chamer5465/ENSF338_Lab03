import random
import timeit
from statistics import median
from matplotlib import pyplot as plt

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

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

def main():
    avg_bubble_best_times = []
    avg_bubble_worst_times = []
    avg_bubble_avg_times = []

    avg_quick_best_times = []
    avg_quick_worst_times = []
    avg_quick_avg_times = []
    
    for i in range (5, 101, 5):
        data = [j for j in range(i)]
        shuffled_data = data.copy()
        reversed_data = list(reversed(data))
        random.shuffle(shuffled_data)
        shuffled_median = int(median(shuffled_data))

        avg_bubble_time_best_case = timeit.timeit(lambda:bubble_sort(data.copy()), number = 100) / 100
        avg_quick_time_best_case = timeit.timeit(lambda:quick_sort(shuffled_data.copy(),shuffled_median ,shuffled_median + 1 ), number = 100) / 100

        avg_bubble_time_worst_case = timeit.timeit(lambda:bubble_sort(reversed_data.copy()), number = 100) / 100
        avg_quick_time_worst_case = timeit.timeit(lambda:quick_sort(reversed_data.copy(), 0, len(data) - 1), number = 100) / 100

        avg_bubble_time_avg_case = timeit.timeit(lambda:bubble_sort(shuffled_data.copy()), number = 100) / 100
        avg_quick_time_avg_case = timeit.timeit(lambda:quick_sort(shuffled_data.copy(), len(data)//2 , len(data)//2 + 1), number = 100) / 100

        avg_bubble_best_times.append(avg_bubble_time_best_case)
        avg_bubble_worst_times.append(avg_bubble_time_worst_case)
        avg_bubble_avg_times.append(avg_bubble_time_avg_case)

        avg_quick_best_times.append(avg_quick_time_best_case)
        avg_quick_worst_times.append(avg_quick_time_worst_case)
        avg_quick_avg_times.append(avg_quick_time_avg_case)

        print(f'The average bubble sort time for an array of {i} elemets is {avg_bubble_time_best_case} using the best conditions.')
        print(f'The average bubble sort time for an array of {i} elemets is {avg_bubble_time_worst_case} using the worst conditions.')
        print(f'The average bubble sort time for an array of {i} elemets is {avg_bubble_time_avg_case} using average conditions.\n')

        print(f'The average quick sort time for an array of {i} elemets is using a random pivot is {avg_quick_time_avg_case} using the best conditions.')
        print(f'The average quick sort time for an array of {i} elemets is using a the lowest element as the pivot is {avg_quick_time_worst_case} using the worst conditions.')
        print(f'The average quick sort time for an array of {i} elemets is {avg_quick_time_best_case} using average conditions.')

    x = [i for i in range(5, 101, 5)]
    plt.figure(num=1, figsize= (20, 10))

    plt.subplot(1, 3, 1)
    plt.plot(x, avg_bubble_avg_times, label= "Average Bubble Sort Case", color='#3b86ff')
    plt.plot(x, avg_quick_avg_times, label= "Average Quick Sort Case", color='#ff3b55')
    plt.title("Average Times for Quick Sort & Bubble Sort")
    plt.legend(loc="upper left")
    plt.xlabel("Size of Array")
    plt.ylabel("Time")
    
    plt.subplot(1, 3, 2)
    plt.plot(x, avg_bubble_best_times, label= "Best Bubble Sort Case", color='#3bfff5')
    plt.plot(x, avg_quick_best_times, label= "Best Quick Sort Case", color='#ffd53b')
    plt.title("Average Times for the best case of Quick Sort & Bubble Sort")
    plt.legend(loc="upper left")
    plt.xlabel("Size of Array")
    plt.ylabel("Time")
    
    plt.subplot(1, 3, 3)
    plt.plot(x, avg_quick_worst_times, label= "Worst Quick Sort Case", color='#ed7d40')
    plt.plot(x, avg_bubble_worst_times, label= "Worst Bubble Sort Case", color='#3bff6c')
    plt.title("Average Times for the worst case of Quick Sort & Bubble Sort")
    plt.legend(loc="upper left")
    plt.xlabel("Size of Array")
    plt.ylabel("Time")

    plt.show()
    plt.close()


if __name__ == '__main__':
    main()