"""GB-6: Student Record Management using a singly linked list."""


class Node:
    def __init__(self, roll, name, marks):
        self.roll, self.name, self.marks = roll, name, marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add(self, roll, name, marks):
        if self.search(roll):
            print("Roll number already exists.")
            return
        node = Node(roll, name, marks)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def delete(self, roll):
        cur, prev = self.head, None
        while cur:
            if cur.roll == roll:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                print("Record deleted.")
                return
            prev, cur = cur, cur.next
        print("Record not found.")

    def update(self, roll, name, marks):
        node = self.search(roll)
        if node:
            node.name, node.marks = name, marks
            print("Record updated.")
        else:
            print("Record not found.")

    def search(self, roll):
        cur = self.head
        while cur:
            if cur.roll == roll:
                return cur
            cur = cur.next
        return None

    def sort(self, by="roll", reverse=False):
        """Bubble sort by swapping node data."""
        if not self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            cur = self.head
            while cur.next:
                a, b = getattr(cur, by), getattr(cur.next, by)
                if (a < b) if reverse else (a > b):
                    cur.roll, cur.next.roll = cur.next.roll, cur.roll
                    cur.name, cur.next.name = cur.next.name, cur.name
                    cur.marks, cur.next.marks = cur.next.marks, cur.marks
                    swapped = True
                cur = cur.next

    def display(self):
        if not self.head:
            print("No records.")
            return
        print(f"{'Roll':<8}{'Name':<15}{'Marks':<8}")
        cur = self.head
        while cur:
            print(f"{cur.roll:<8}{cur.name:<15}{cur.marks:<8}")
            cur = cur.next


sl = StudentList()
while True:
    print("\n1.Add 2.Delete 3.Update 4.Search 5.Sort & Display 6.Display 0.Exit")
    ch = input("Choice: ")
    if ch == "1":
        sl.add(int(input("Roll: ")), input("Name: "), float(input("Marks: ")))
    elif ch == "2":
        sl.delete(int(input("Roll to delete: ")))
    elif ch == "3":
        sl.update(int(input("Roll to update: ")), input("New name: "), float(input("New marks: ")))
    elif ch == "4":
        n = sl.search(int(input("Roll to search: ")))
        print(f"Found: {n.roll}, {n.name}, {n.marks}" if n else "Not found.")
    elif ch == "5":
        by = "marks" if input("Sort by (1=Roll, 2=Marks): ") == "2" else "roll"
        rev = input("Order (1=Ascending, 2=Descending): ") == "2"
        sl.sort(by, rev)
        sl.display()
    elif ch == "6":
        sl.display()
    elif ch == "0":
        break
