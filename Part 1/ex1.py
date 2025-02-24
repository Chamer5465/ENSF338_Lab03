
def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    
    L = [0] * n1
    H = [0] * n2
    
    for i in range(n1):
        L[i] = arr[low + i]
    for j in range(n2):
        H[j] = arr[mid + 1 + j]
    
    i = 0 # temp index
    j = 0 # temp index
    k = low # main index
    
    while i < n1 and j < n2:
        if L[i] <= H[j]:
            arr[k] = L[i]
            i += 1
            
        else:
            arr[k] = H[j]
            j += 1
        k += 1
            
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = H[j]
        j += 1
        k += 1

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1, high)
        merge(arr, low, mid, high)
        
def print_list(arr):
    for i in arr:
        print(i, end=", ")
    print()
    
def main():
    arr = [6, 42, 25, 3, 3, 2, 27, 3]
    print("Original Array:")
    print_list(arr)

    merge_sort(arr, 0, len(arr) - 1)

    print("Sorted Array:")
    print_list(arr)

if __name__ == "__main__":
    main()
