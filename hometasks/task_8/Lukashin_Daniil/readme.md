# Task A, method 3

Run file - python3 task_a_method_3.py

Depends files - file_for_task_b.txt ```Its file with text for searching```

Use value ```keyword``` in main for setting word for searching

Output data printed in terminal

### Example output:
keyword = sweet
```
is so sweet to him,
every moment, sweet fruit for
```

# Task B, method 4

Run file - python3 task_b_method_4.py

Output data printed in terminal and created file task_b_output.txt

### Example output:
```
Solution found 92:
. . . . . . . Q
. . . Q . . . .
Q . . . . . . .
. . Q . . . . .
. . . . . Q . .
. Q . . . . . .
. . . . . . Q .
. . . . Q . . .

--------------------
```

# Compare analysis

## KWIC (Key Word in Context)

| Criterion | Multiprocessing and pipes | Main/Subroutine | Abstract Data types |
|----------|-------------------------|---------------------|------------------------|
| a) Changing the algorithm | Is difficult, since the logic is distributed between processes | **Easy**, thanks to the clear separation of routines | On average, it depends on the connectivity of classes |
| b) Changing the presentation of data | **Easy**, due to the independence of processes | Difficult, requires changes in all routines | **Easy**, through changing class interfaces |
| c) Adding functions | Medium, requires the creation of new processes | **Easy**, through the addition of new routines | **Easy**, through the expansion of classes |
| d) Performance | **High**, thanks to parallel processing | Average | Average |
| e) Reusability | Average, depends on the specifics of the task | High for similar tasks | **Very high**, thanks to OOP |

## Eight Queens (8Q)

| Criterion | Asynchronous solution | Abstract Data types | Pipes and Filters |
|----------|-------------------|------------------------|-----------------|
| a) Changing the algorithm | Difficult due to asynchronous logic | **Easy** due to encapsulation | Medium, requires changing filters |
| b) Changing the data representation | Medium | **Easy**, through changing classes | **Easy**, due to the independence of filters |
| c) Adding functions | Difficult due to asynchrony | **Easy**, through adding methods | **Easy**, through adding new filters |
| d) Performance | **High** for I/O operations | Medium | High for sequential processing |
| e) Overuse | Low | **High** | Average |

### Conclusions:
1. For KWIC, the most flexible and reused solution is using abstract data types.
2. For Eight Queens, the abstract data type solution also provides a better balance between flexibility and ease of modification.
3. Performance is better in parallel processing solutions (multiprocessing for KWIC and asynchrony for 8Q).