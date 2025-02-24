import json
import time
import matplotlib.pyplot as plt

def binary_search(arr, key, initial_mid):

    low = 0
    high = len(arr) - 1
    if low <= initial_mid <= high:
        mid = initial_mid
    else:
        mid = (low + high) // 2

    while low <= high:
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high) // 2 
    return -1

def main():
    with open('ex7data.json', 'r') as f:
        data = json.load(f)

    with open('ex7tasks.json', 'r') as f:
        tasks = json.load(f)

    iterations = 2

    tasks_values=[]
    best_initials=[]

    for task in tasks: 
        best_time = 1
        best_mid = None
        for mid in range(0,max(data),500): 
            start = time.perf_counter()
            for j in range(iterations):
                binary_search(data, task, mid)
            elapsed = (time.perf_counter() - start) / iterations

            if elapsed < best_time:
                best_time = elapsed
                best_mid = mid
            
        tasks_values.append(task)
        best_initials.append(best_mid)

        print(f"Task: {task}, Best initial midpoint: {best_mid}, Time: {best_time:.8f} sec")

    plt.figure(figsize=(10, 6))
    plt.scatter(tasks_values, best_initials, color='blue', alpha=0.7)
    plt.xlabel('Search Task (Key)')
    plt.ylabel('Best Initial Midpoint')
    plt.title('Scatterplot: Best Initial Midpoint vs. Search Task')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()


'''
There appears to be a correlation between the best midpoint and the key as 
if the key is closer to the beggining the lower midpoint minimizes the number of comparisons, 
if the key is closer to the end the higher midpoint minimizes the number of comparisons.
Binary search halves the array every iteration and removing a few steps can reduce the comparisons required immediately, though it mostly helps when the key is near the beggining or end of the dataset.
'''