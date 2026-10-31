"""GB-5: Real-time event processing using a Queue."""
from collections import deque

queue = deque()


def add_event(e):
    queue.append(e)                      # enqueue: O(1)
    print(f"Event '{e}' added.")


def process_event():
    if not queue:
        print("No events to process.")
        return
    print(f"Processing event: '{queue.popleft()}'")   # dequeue: O(1)


def display_events():
    if not queue:
        print("No pending events.")
        return
    print("Pending events (front -> rear):", list(queue))


def cancel_event(e):
    if e in queue:
        queue.remove(e)                  # O(n)
        print(f"Event '{e}' cancelled.")
    else:
        print("Event not found (already processed or never added).")


while True:
    print("\n1.Add event  2.Process next  3.Display pending  4.Cancel event  0.Exit")
    ch = input("Choice: ")
    if ch == "1":
        add_event(input("Event name: "))
    elif ch == "2":
        process_event()
    elif ch == "3":
        display_events()
    elif ch == "4":
        cancel_event(input("Event to cancel: "))
    elif ch == "0":
        break
