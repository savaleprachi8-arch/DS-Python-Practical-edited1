"""GA-1: Library borrowing records (average, highest/lowest, zero borrowers, mode)."""

members = {"Amit": 5, "Neha": 0, "Ravi": 3, "Sara": 0, "John": 3, "Priya": 7}
books = {"DSA": 12, "Python": 20, "DBMS": 8, "OS": 8, "Networks": 3}


def average_borrowed():
    # Time: O(n)   Space: O(1)
    return sum(members.values()) / len(members) if members else 0


def highest_lowest():
    # Time: O(n)   Space: O(1)
    hi = max(books, key=books.get)
    lo = min(books, key=books.get)
    return hi, books[hi], lo, books[lo]


def zero_borrowers():
    # Time: O(n)   Space: O(1)
    return sum(1 for c in members.values() if c == 0)


def mode_of_borrows():
    # Time: O(n)   Space: O(n)  (frequency table)
    freq = {}
    for c in books.values():
        freq[c] = freq.get(c, 0) + 1
    max_f = max(freq.values())
    modes = [c for c, f in freq.items() if f == max_f]
    most_borrowed = max(books, key=books.get)
    return modes, max_f, most_borrowed


def add_data():
    n = int(input("How many members to add? "))
    for _ in range(n):
        name = input("  Member name: ")
        members[name] = int(input("  Books borrowed: "))
    n = int(input("How many books to add? "))
    for _ in range(n):
        name = input("  Book title: ")
        books[name] = int(input("  Times borrowed: "))


while True:
    print("\n1.Average borrowed  2.Highest/Lowest book  3.Members with 0 borrows"
          "\n4.Mode / most frequently borrowed  5.Add data  6.Show data  0.Exit")
    ch = input("Choice: ")
    if ch == "1":
        print("Average books borrowed per member:", round(average_borrowed(), 2))
        print("Time O(n), Space O(1)")
    elif ch == "2":
        h, hc, l, lc = highest_lowest()
        print(f"Highest: {h} ({hc})   Lowest: {l} ({lc})")
        print("Time O(n), Space O(1)")
    elif ch == "3":
        print("Members with zero borrows:", zero_borrowers())
        print("Time O(n), Space O(1)")
    elif ch == "4":
        modes, f, mb = mode_of_borrows()
        print(f"Mode of borrow counts: {modes} (appears {f} times)")
        print("Most frequently borrowed book:", mb)
        print("Time O(n), Space O(n)")
    elif ch == "5":
        add_data()
    elif ch == "6":
        print("Members:", members)
        print("Books:", books)
    elif ch == "0":
        break
