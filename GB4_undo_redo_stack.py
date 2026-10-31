"""GB-4: Undo/Redo system using stacks."""


class TextEditor:
    def __init__(self):
        self.document = []      # current changes (acts as the state)
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, text):
        self.document.append(text)
        self.undo_stack.append(text)
        self.redo_stack.clear()          # new change invalidates redo history

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        change = self.undo_stack.pop()
        self.document.pop()
        self.redo_stack.append(change)
        print(f"Undid: '{change}'")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        change = self.redo_stack.pop()
        self.document.append(change)
        self.undo_stack.append(change)
        print(f"Redid: '{change}'")

    def display(self):
        print("Document:", " ".join(self.document) if self.document else "<empty>")


ed = TextEditor()
while True:
    print("\n1.Make change  2.Undo  3.Redo  4.Display  0.Exit")
    ch = input("Choice: ")
    if ch == "1":
        ed.make_change(input("Enter text: "))
    elif ch == "2":
        ed.undo()
    elif ch == "3":
        ed.redo()
    elif ch == "4":
        ed.display()
    elif ch == "0":
        break
