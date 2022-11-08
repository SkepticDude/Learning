arr = [48,36,34,23,17,7]

def SelectionSort(arr):
    print("Given Array :",arr)
    print("\nStarting Selection Sort...")
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        #print("After Pass",i+1,":",arr)
    return arr

print("Result :",SelectionSort(arr))


# Given Array : [48, 36, 34, 23, 17, 7]

# Starting Selection Sort...

# At the Start : [48, 36, 34, 23, 17, 7]    5 comparisons
# index :         0   1   2   3   4   5
# After Pass 1 : [7| 36, 34, 23, 17, 48]    4 comparisons
# After Pass 2 : [7, 17| 34, 23, 36, 48]    3 comparisons
# After Pass 3 : [7, 17, 23| 34, 36, 48]    2 comparisons
# After Pass 4 : [7, 17, 23, 34| 36, 48]    1 comparisons
# After Pass 5 : [7, 17, 23, 34, 36| 48]

# 1 + 2 + 3 + 4 + ... + (n-1)   Same as BubbleSort
# AP Series

# Time Complexity : O(n^2), θ(n^2), Ω(n^2)
# Wrost Case =>     Big O
# Average Case =>   Theta θ
# Best Case =>      Omega Ω

# Space Complexity (Auxilary Size) = O(1)
# Space Complexity (Auxilary Size + Input Size) = O(n)

# Unstable Algorithm (Order of same elements is not maintained)
# not Adaptive
# Less number of Swaps