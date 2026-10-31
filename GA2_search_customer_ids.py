"""GA-2: Linear search and binary search on customer account IDs."""


def linear_search(arr, key):
    # Time: O(n)   Space: O(1)
    for i, v in enumerate(arr):
        if v == key:
            return i
    return -1


def binary_search(arr, key):
    # Requires sorted list.  Time: O(log n)   Space: O(1)
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


ids = [int(x) for x in input("Enter customer IDs (space separated): ").split()]
while True:
    print("\n1.Linear search  2.Binary search  0.Exit")
    ch = input("Choice: ")
    if ch == "0":
        break
    if ch in ("1", "2"):
        key = int(input("Account ID to search: "))
        if ch == "1":
            pos = linear_search(ids, key)
        else:
            sorted_ids = sorted(ids)
            pos = binary_search(sorted_ids, key)
        print(f"ID {key} {'found at index ' + str(pos) if pos != -1 else 'NOT found'}")
