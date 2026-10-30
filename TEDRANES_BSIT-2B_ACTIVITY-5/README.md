# Module 5 Laboratory Activity: Stacks and Queues

## Project Description
This project demonstrates four fundamental data structure implementations in Python:
- ArrayStack (fixed-size array, LIFO)
- LinkedStack (linked list, LIFO)
- Circular ArrayQueue (fixed-size circular array, FIFO)
- LinkedQueue (linked list with front and rear references, FIFO)

It also includes a menu-driven program, a parentheses balance checker, and a print queue simulation.

## Requirements
- Python 3.8 or later
- No external packages are required.

## Project Files
| File | Description |
|---|---|
| `array_stack.py` | Array-based stack with push, pop, peek, is_empty, and is_full |
| `linked_stack.py` | Linked-list stack with push, pop, peek, and is_empty |
| `array_queue.py` | Circular array queue with enqueue, dequeue, peek_front, is_empty, and is_full |
| `linked_queue.py` | Linked-list queue with front and rear references |
| `main.py` | Menu-driven program for selecting an implementation and performing operations |
| `analysis.md` | Written answer to the laboratory analysis question |

## How to Run

Open a terminal in this folder.

### 1. Main menu-driven program
```bash
python main.py
```
Choose 1 for ArrayStack, 2 for LinkedStack, 3 for Circular ArrayQueue, or 4 for LinkedQueue. Follow the displayed operation menu.

### 2. Run tests
```bash
python test_driver.py
```
The test driver checks stack and queue operations, underflow and overflow handling, circular queue wrap-around, linked queue empty-state handling, and parentheses matching.

## Error Handling
The array implementations raise `OverflowError` when full. Stack and queue removal or peek operations raise `IndexError` when empty. The menu and print queue display descriptive error messages.

## Data Structure Principles
- **Stack – LIFO:** Last In, First Out. Insertion and removal happen at the top.
- **Queue – FIFO:** First In, First Out. Insertion happens at the rear and removal happens at the front.
- **Circular queue:** Modulo arithmetic reuses available array positions after wrap-around.
