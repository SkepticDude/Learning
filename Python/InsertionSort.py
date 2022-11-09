arr = [9,13,7,4,18,3]

def InsertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
        print("After Pass",i,":",arr)
    return arr

print(InsertionSort(arr))

#               <-sorted | unsorted->  
# Before Start : [9| 13, 7, 4, 18, 3]   1 comparison
# After Pass 1 : [9, 13| 7, 4, 18, 3]   2 comparisons
# After Pass 2 : [7, 9, 13| 4, 18, 3]   3 comparisons
# After Pass 3 : [4, 7, 9, 13| 18, 3]   4 comparisons
# After Pass 4 : [4, 7, 9, 13, 18| 3]   5 comparisons
# After Pass 5 : [3, 4, 7, 9, 13, 18]

# Possible Swaps : (n-1)
# Maximum Comparisons = 1 + 2 + 3 + 4 + 5
# 1 + 2 + 3 +...+ (n-1) comparisons


# AP Series
# Time complexity = O(n^2), θ(n^2), Ω(n)
# Wrost Case =>     Big O
# Average Case =>   Theta θ
# Best Case =>      Omega Ω

# Space Complexity (Auxilary Size) = O(1)
# Space Complexity (Auxilary Size + Input Size) = O(n)

# Stable Algorithm (Order of same elements is maintained)
# Adaptive
# Lesser swaps compared to Bubble Sort
