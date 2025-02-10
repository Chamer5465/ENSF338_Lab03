import random
import timeit

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

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
    for i in range (100, 2001, 100):
        data = [j for j in range(i)]
        shuffled_data = random.shuffle(data)
        reversed_data = data.reverse()

        avg_bubble_time_avg_case = timeit.timeit(lambda:bubble_sort(data), number = 100) / 100
        avg_quick_time_avg_case = timeit.timeit(lambda:quick_sort(data, 0, len(data) - 1), number = 100) / 100

        print(f'The average bubble sort time for a sorted array of {i} elemets is {avg_bubble_time_avg_case}.')
        print(f'The average quick sort time for an array of {i} elemets is {avg_quick_time_avg_case}.')

if __name__ == '__main__':
    main()