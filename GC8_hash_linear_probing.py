"""GC-8: Hash table, division method, collision resolution by linear probing."""

SIZE = int(input("Enter table size: "))
EMPTY, DELETED = None, "<deleted>"
table = [EMPTY] * SIZE


def hash_fn(key):
    return key % SIZE                    # division method


def insert(key):
    idx = hash_fn(key)
    for i in range(SIZE):
        pos = (idx + i) % SIZE
        if table[pos] == key:
            print("Key already present.")
            return
        if table[pos] in (EMPTY, DELETED):
            table[pos] = key
            print(f"Inserted at index {pos}.")
            return
    print("Table is full!")


def search(key):
    idx = hash_fn(key)
    for i in range(SIZE):
        pos = (idx + i) % SIZE
        if table[pos] == EMPTY:
            return -1
        if table[pos] == key:
            return pos
    return -1


def delete(key):
    pos = search(key)
    if pos == -1:
        print("Key not found.")
    else:
        table[pos] = DELETED
        print(f"Deleted from index {pos}.")


def display():
    for i, v in enumerate(table):
        print(f"{i}: {v if v is not None else '-'}")


while True:
    print("\n1.Insert  2.Search  3.Delete  4.Display  0.Exit")
    ch = input("Choice: ")
    if ch == "1":
        insert(int(input("Key: ")))
    elif ch == "2":
        p = search(int(input("Key to search: ")))
        print(f"Found at index {p}" if p != -1 else "Not found.")
    elif ch == "3":
        delete(int(input("Key to delete: ")))
    elif ch == "4":
        display()
    elif ch == "0":
        break
