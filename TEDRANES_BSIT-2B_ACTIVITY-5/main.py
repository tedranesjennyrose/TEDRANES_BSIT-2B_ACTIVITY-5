from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def display_state(structure, kind):
    if kind == "ArrayStack":
        items = structure.data[:structure.top + 1]
        print("Stack (bottom to top):", items)

    elif kind == "LinkedStack":
        items = []
        current = structure.top
        while current is not None:
            items.append(current.value)
            current = current.next
        print("Stack (top to bottom):", items)

    elif kind == "ArrayQueue":
        items = []
        for i in range(structure.size):
            index = (structure.front + i) % len(structure.data)
            items.append(structure.data[index])
        print("Queue (front to rear):", items)

    elif kind == "LinkedQueue":
        items = []
        current = structure.front
        while current is not None:
            items.append(current.value)
            current = current.next
        print("Queue (front to rear):", items)


def main():
    print("================================")
    print("     STACKS AND QUEUES SYSTEM")
    print("================================")
    print("1. ArrayStack")
    print("2. LinkedStack")
    print("3. Circular ArrayQueue")
    print("4. LinkedQueue")

    choice = input("Choose implementation (1-4): ").strip()

    if choice == "1":
        structure, kind = ArrayStack(5), "ArrayStack"
    elif choice == "2":
        structure, kind = LinkedStack(), "LinkedStack"
    elif choice == "3":
        structure, kind = ArrayQueue(5), "ArrayQueue"
    elif choice == "4":
        structure, kind = LinkedQueue(), "LinkedQueue"
    else:
        print("Invalid choice!")
        return

    while True:
        print("\\n================================")
        print("       OPERATION MENU")
        print("================================")
        if "Stack" in kind:
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
        else:
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek Front")

        print("4. Check if Empty")
        print("5. Check if Full")
        print("6. Exit")

        operation = input("Enter your choice: ").strip()

        try:
            if operation == "1":
                value = input("Enter value: ")
                if "Stack" in kind:
                    structure.push(value)
                else:
                    structure.enqueue(value)
                print("Element inserted successfully!")

            elif operation == "2":
                if "Stack" in kind:
                    print("Removed:", structure.pop())
                else:
                    print("Removed:", structure.dequeue())

            elif operation == "3":
                if "Stack" in kind:
                    print("Top element:", structure.peek())
                else:
                    print("Front element:", structure.peek_front())

            elif operation == "4":
                print("Is Empty:", structure.is_empty())

            elif operation == "5":
                if hasattr(structure, "is_full"):
                    print("Is Full:", structure.is_full())
                else:
                    print("Linked structures have no fixed capacity.")

            elif operation == "6":
                print("Thank you for using the system!")
                break

            else:
                print("Invalid operation. Please select 1-6.")

            display_state(structure, kind)

        except (IndexError, OverflowError) as error:
            print("Error:", error)
            display_state(structure, kind)


if __name__ == "__main__":
    main()
