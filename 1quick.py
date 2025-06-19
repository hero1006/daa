import time
import random

def quick(arr):
    if len(arr) <= 1:
        return arr
    piv = arr[len(arr) // 2]
    low = [x for x in arr if x < piv]
    mid = [x for x in arr if x == piv]
    high = [x for x in arr if x > piv]
    return quick(low) + mid  + quick(high)


def calc_time(arr):
    
    start = time.time()
    quick(arr)
    avg_time = time.time() - start


    start = time.time()
    quick(sorted(arr))
    best_time = time.time() - start

    
    start = time.time()
    quick(sorted(arr, reverse=True))
    worst_time = time.time() - start

    return best_time, avg_time, worst_time


test_sizes = [random.randint(1, 100000) for _ in range(10)]
print("\n\tBest_Case\tAverage_Case\tWorst_Case")

for n in test_sizes:
    arr = [random.randint(1, 100000) for _ in range(n)]
    best_time, avg_time, worst_time = calc_time(arr)
    print(f"{n}\t{best_time:.6f}\t{avg_time:.6f}\t{worst_time:.6f}")

