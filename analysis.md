# Programming Assignment 2: Analysis

Name: Cecilia XING

How to fill this in:
* Write your answer after each `ANSWER:` marker, on the same line and/or the lines below it.
  Keep it above the next heading. Delete the "(replace this ...)" text.
* Do NOT delete or rename the `ANSWER:` markers.
* Diagrams can be plain text. For example, an array with three values and one empty slot: `[ a | b | c | _ ]`
* Use your own words and your own numbers. Short, specific answers are better than long vague ones.

## Part A: On paper (do this before you write code)

### A1
Draw an array list with capacity 4 holding 'a', 'b', 'c' (size 3). Use `_` for an empty slot.
Now draw it after `array_list_insert_at(lst, 1, 'x')`. How many values were shifted, so what
should 'moves' be?

ANSWER: 
Before: [ a | b | c | _ ]
After:  [ a | x | b | c ]

### A2
Start again from a FULL array list: capacity 4 holding 'a', 'b', 'c', 'd'. Draw the array after
`array_list_insert_at(lst, 4, 'x')`. What is the capacity now? How many values were copied?
Why can inserting at the END cost a lot sometimes, and almost nothing other times?

ANSWER: 
Before: [ a | b | c | d ]
After:  [ a | b | c | d | x | _ | _ | _ ]
Capacity now: 8
Values copied: 4
Why inserting at the end costs vary: When there is still remaining capacity in the array, inserting at the end does not require moving any existing elements. Instead, new elements are directly placed in the next empty slot, with a time complexity of O(1). When the array is full, expansion is triggered, and all $n$elements in the original array are copied one by one to the new memory space, with a time complexity of O(n).
### A3
Draw the linked list a -> b -> c (show 'head', 'size', and the nodes with their links). Draw it
again after `linked_list_insert_at(lst, 1, 'x')`. Which links changed? How many?

ANSWER: 
Before:
head ---> [ a | next ] ---> [ b | next ] ---> [ c | next ] ---> None
size = 3
After:
head -> [ a | next ] -> [ x | next ] -> [ b | next ] -> [ c | next ] ---> None
size = 4
Links changed: 2 links changed.
1. Node 'a' changes its next pointer to node 'x'.
2. The new node 'x' sets its next pointer to node 'b'.

### A4
Which structure does less work to remove the value at index 0: the array list or the linked
list? Which does less work to get the value at index 2? Explain in a sentence or two.

ANSWER: 
Removing the value at index 0: The linked list does less work ($O(1)$) because it only needs to update the head pointer to the second node, whereas the array list ($O(n)$) must shift all remaining elements one position to the left.
Getting the value at index 2: The array list does less work ($O(1)$) because it uses direct memory indexing (data[2]), whereas the linked list ($O(n)$) must sequentially traverse pointers starting from the head node to reach index 2.

## Part D: Timing

### Step 1: Predictions (write these BEFORE you run timing.py)
You will not lose points for a wrong prediction. The point is to notice when you are surprised.

### P1
At n = 100,000, which is faster at inserting a value at the FRONT: Python's built-in list or your
linked list? About how many times faster?

ANSWER: The linked list is faster. Inserting at the front of a linked list takes $O(1)$ time (only updating the head pointer), whereas Python's built-in list takes $O(n)$ time to shift all $n$ elements. At $n = 100,000$, the linked list is expected to be about 10 to 40 times faster.
### P2
At n = 100,000, which is faster at getting the MIDDLE value: your array list or your linked
list? About how many times faster?

ANSWER: Your array list is faster. Getting an element by index in an array list takes $O(1)$ direct memory access time, whereas a linked list takes $O(n)$ time because it must traverse pointers sequentially from the head to index $n/2$. At $n = 100,000$, the array list is expected to be about 2,000 to 3,000 times faster.
### P3
Python's list and array.array can both hold 1,000 whole numbers. Which one do you think uses less
memory, and about how many times less?

ANSWER: array.array uses less memory. A standard Python list holds pointers to integer objects (each incurring object overhead), whereas array.array stores raw C-style integers directly in contiguous memory. array.array uses about 8 to 9 times less memory in total.
### Step 2: Time it yourself (my_timing.py)

### T1
Run `python3 my_timing.py` and paste the table it printed. Then explain: for small n, which of the
two columns (stopwatch or timeit) do you trust more, and why does running something many times
and averaging help?

ANSWER: 
microseconds per operation
  structure                  n=100       n=1,000      n=10,000     n=100,000
  your array_list             0.09          0.11          0.13          0.17
  your linked_list            0.89          9.57         98.42      1,133.06
  Python list                 0.01          0.01          0.01          0.02
  array.array                 0.02          0.02          0.02          0.03
  deque                       0.01          0.01          0.01          0.02

I trust the timeit column more, especially for small $n$. Measuring a single operation with a stopwatch (time.perf_counter) can easily be skewed by background CPU tasks, OS thread scheduling, or garbage collection. Running the operation many times and taking the average smooths out these transient spikes and yields a far more reliable, repeatable measurement.
### Step 3: The experiment (timing.py)
Run `python3 timing.py` and paste ALL of its output between the lines of backticks below.

### Your results

```text
Python 3.14.0
Sizes: 100, 1,000, 10,000, 100,000
  timing your array_list ...
  timing your linked_list ...
  timing Python list ...
  timing array.array ...
  timing deque ...

Insert a value at the FRONT (index 0)
  microseconds per operation
  structure                  n=100       n=1,000      n=10,000     n=100,000
  your array_list             2.65         27.00        265.94      2,689.57
  your linked_list            0.09          0.09          0.10          0.44
  Python list                 0.03          0.17          1.54         16.69
  array.array                 0.03          0.06          0.39          5.60
  deque                       0.01          0.01          0.01          0.02

Get the MIDDLE value (index n // 2)
  microseconds per operation
  structure                  n=100       n=1,000      n=10,000     n=100,000
  your array_list             0.04          0.06          0.07          0.25
  your linked_list            0.46          4.48         47.69        574.67
  Python list                 0.02          0.02          0.02          0.03
  array.array                 0.02          0.03          0.03          0.05
  deque                       0.02          0.03          0.08          2.18

Insert a value at the END
  microseconds per operation
  structure                  n=100       n=1,000      n=10,000     n=100,000
  your array_list             0.09          0.11          0.13          0.17
  your linked_list            0.89          9.57         98.42      1,133.06
  Python list                 0.01          0.01          0.01          0.02
  array.array                 0.02          0.02          0.02          0.03
  deque                       0.01          0.01          0.01          0.02

Memory for 1,000 whole numbers (0 .. 999)
  Python list:  8,056 bytes for the list itself
               + about 28,000 bytes for the int objects it points to
  array.array:  4,200 bytes (the numbers are stored directly in the array)

Copy ALL of this output into analysis.md.
```

### Q1
Pick ONE operation on ONE of YOUR structures (for example, get the middle value of your linked
list). How did its time change as n went from 1,000 to 10,000 to 100,000? Does the change match
its Big-O? Give the numbers and the ratio.

ANSWER: 
I choose getting the middle value of my linked list.
- Measured times:
  - $n = 1,000$: $4.48\ \mu\text{s}$
  - $n = 10,000$: $47.69\ \mu\text{s}$ (Ratio: $ \approx 10\times$)
  - $n = 100,000$: $574.67\ \mu\text{s}$ (Ratio: $\approx 12\times$)
- Big-O Analysis:
Finding the middle element in a linked list requires traversing $n/2$ links, which is $O(n)$. When $n$ increases by a factor of 10, the runtime increases by roughly 10 to 12 times, which perfectly aligns with linear time complexity $O(n)$.
### Q2
For inserting at the front, at about what n does your linked list become faster than Python's
built-in list? (Look between the sizes in the table.) Why does Python's list win for small n,
even though its Big-O is worse?

ANSWER: 
My linked list becomes faster than Python's built-in list between $n = 100$ and $n = 1,000$ (at $n=100$, Python list takes $0.03\ \mu\text{s}$ vs. linked list $0.09\ \mu\text{s}$; at $n=1,000$, Python list takes $0.17\ \mu\text{s}$ vs. linked list $0.09\ \mu\text{s}$).Python's built-in list wins for small $n$ because it is implemented in highly optimized C code, which has extremely low constant factor overhead. In contrast, our custom linked list creates Python dictionary objects and performs dynamic attribute/key lookups in pure Python code.
### Q3
Inserting at the front of Python's list and of your array list are both O(n), but Python's is much
faster. Why?

ANSWER: 
Python's built-in list is implemented entirely in C (PyListObject). Shifting pointers in C is executed via low-level memory block moves (memmove), which utilize vector CPU instructions. Our pure Python array_list executes an explicit Python for loop that reads and writes dictionary keys one element at a time, introducing significant Python interpreter and dynamic lookup overhead
### Q4
array.array and Python's list are both O(n) at the front, but array.array is a few times faster.
Use the memory numbers to explain why.

ANSWER: 
array.array stores primitive numerical values directly in a contiguous block of memory ($4,200$ bytes total), whereas Python's list stores pointers to heap-allocated Python integer objects ($36,056$ bytes total). Because array.array occupies significantly less memory, it exhibits superior CPU cache locality and needs to shift far fewer raw bytes during front insertions.
### Q5
Getting the middle value of a deque and of your linked list are both O(n), but the deque is far
faster at large n. What do you think is different about how they are built?

ANSWER: 
Python's collections.deque is implemented as a doubly-linked list of fixed-size blocks/arrays (blocks of 62 elements) in C, rather than individual single-node allocations. This hybrid block structure allows the deque to jump directly across whole blocks of elements during indexing, dramatically reducing pointer chasing and improving memory locality.
### Q6
Which of the five structures would you choose for (a) 1,000,000 values that are read by index all
day and almost never changed, and (b) a line of tasks where new ones are added at the back and
finished ones are removed from the FRONT, millions of times? Explain each.

ANSWER: 
- (a) 1,000,000 values read by index: Python list (or array.array for pure numbers). Both provide instantaneous $O(1)$ random access, contiguous memory allocation, and minimal lookup overhead.
- (b) Task queue (add back, remove front millions of times): collections.deque. It provides $O(1)$ amortized time complexity for both append and popleft operations at native C performance, making it ideal for FIFO queue operations.
### Q7
What surprised you most in these results, and what does it tell you about predicting performance?

ANSWER: 
What surprised me most was how fast Python's $O(n)$ built-in operations (like inserting at the front of a list) are compared to a pure Python $O(1)$ linked list for small $n$. This demonstrates that Big-O complexity only describes scalability trends as $n \to \infty$; implementation language, constant factors, memory layout, and CPU cache locality play a critical role in real-world runtime performance.