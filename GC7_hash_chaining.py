"""GC-7: Hash table (size 10), division method, collision resolution by chaining."""

SIZE = 10
table = [[] for _ in range(SIZE)]


def hash_fn(key):
    return key % SIZE                    # division method


def insert(key, value):
    chain = table[hash_fn(key)]
    for pair in chain:
        if pair[0] == key:
            pair[1] = value              # update existing key
            print("Key existed, value updated.")
            return
    chain.append([key, value])
    print(f"Inserted at index {hash_fn(key)}.")


def search(key):
    for k, v in table[hash_fn(key)]:
        if k == key:
            return v
    return None


def delete(key):
    chain = table[hash_fn(key)]
    for i, (k, _) in enumerate(chain):
        if k == key:
            chain.pop(i)
            print("Deleted.")
            return
    print("Key not found.")


def display():
    for i, chain in enumerate(table):
        print(f"{i}: " + (" -> ".join(f"({k}:{v})" for k, v in chain) if chain else "empty"))


while True:
    print("\n1.Insert  2.Search  3.Delete  4.Display  0.Exit")
    ch = input("Choice: ")
    if ch == "1":
        insert(int(input("Key (integer): ")), input("Value: "))
    elif ch == "2":
        v = search(int(input("Key to search: ")))
        print(f"Value: {v}" if v is not None else "Key not found.")
    elif ch == "3":
        delete(int(input("Key to delete: ")))
    elif ch == "4":
        display()
    elif ch == "0":
        break
