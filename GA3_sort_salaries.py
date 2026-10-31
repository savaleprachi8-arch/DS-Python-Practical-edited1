"""GA-3: Selection sort & bubble sort of salaries, display top 5."""


def selection_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a


def bubble_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


salaries = [float(x) for x in input("Enter salaries (space separated): ").split()]

sel = selection_sort(salaries)
bub = bubble_sort(salaries)
print("Selection sort (ascending):", sel)
print("Bubble sort    (ascending):", bub)
print("Top 5 highest salaries:", sel[::-1][:5])
print("Complexity: Selection O(n^2) time, O(1) space | Bubble O(n^2) worst, O(n) best, O(1) space")
