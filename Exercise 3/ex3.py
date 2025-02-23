import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(array):
    n = len(array)
    comparison=0
    swap=0
    for i in range(n):
        for j in range(0, n-i-1):
            comparison+=1
            if array[j] > array[j + 1]:
                swap+=1
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return comparison,swap

def main():
    avg_comparisons_list=[]
    avg_swaps_list=[]
    repetitions=[]
    for i in range (100, 2001, 100):
        data = [j for j in range(i)]
        repetitions.append(i)
        comparisons_sum=0
        swaps_sum=0
        count=0
        for j in range(0,10):
            count+=1
            shuffled_data = random.shuffle(data)
            reversed_data = data.reverse()

            comparisons, swaps = bubble_sort(data)
            comparisons_sum+=comparisons
            swaps_sum+=swaps
        avg_comparisons_list.append(comparisons_sum/count)
        avg_swaps_list.append(swaps_sum/count)
        print(avg_comparisons_list)
        print(avg_swaps_list)
    

    slope, intercept = np.polyfit(repetitions, avg_comparisons_list, 1)
    line_values = [slope * x + intercept for x in repetitions]

    plt.scatter(repetitions, avg_comparisons_list, color='blue', label='Measured Time')
    plt.plot(repetitions, line_values, color='red', linestyle='dashed', label='Linear Fit')
    plt.title("Average Comparisons")
    plt.xlabel("Size of Shuffled Array")
    plt.ylabel("Average Comparisons For Bubble Sort")
    plt.show()

    slope, intercept = np.polyfit(repetitions, avg_swaps_list, 1)
    line_values = [slope * x + intercept for x in repetitions]

    plt.scatter(repetitions, avg_swaps_list, color='blue', label='Measured Time')
    plt.plot(repetitions, line_values, color='red', linestyle='dashed', label='Linear Fit')
    plt.title("Average Swaps")
    plt.xlabel("Size of Shuffled Array")
    plt.ylabel("Average Swaps For Bubble Sort")
    plt.show()


if __name__ == '__main__':
    main()