arr = [95,86,74,64,59,11]

def BubbleSort(arr: list):
    for i in range(len(arr)-1):
        isSorted = True
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSorted = False
        if isSorted: return arr
    return arr

print(BubbleSort(arr))

# possible swap during passes
# 1st pass => 5 possible swap   (n-1)
# 2nd pass => 4 possible swap   (n-2)
# 3rd pass => 3 possible swap   (n-3)
# 4th pass => 2 possible swap   (n-4)
# 5th pass => 1 possible swap   (n-5)

# Maximum possible swaps = 1 + 2 + 3 + 4 + 5
# AP Series 
# Number of passes (No of columns) = 5 => (n-1)
# first term = 1 , last term = 5
# (1+5) => n

# 2 (1 + 2 + 3 + ... + n) =  (n-1) x n 

#                         (n-1) x n
# 1 + 2 + 3 + ... + n =   ----------  =>  n^2  => O(n^2)
#                             2

# Time complexity = O(n^2)
# Space Complexity (Auxilary Size) = O(1)
# Space Complexity (Auxilary Size + Input Size) = O(n)

# [86,74,64,59,11,95]
# [74,64,59,11,86,95]
# [64,59,11,74,86,95]
# [59,11,64,74,86,95]
# [11,59,64,74,86,95]