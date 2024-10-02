# Write a python program to create a list of roots with at list 15 elements and perform following operations: 
# 1. access link using positive indexing, 
# 2. access link using negative indexing, 
# 3. delete last element of the list, 
# 4. add element at the end of the list, 
# 5. repeat the list using operator, 
# 6. get middle of the element, 
# 7. traverse the entire list. 

import math

# Create a list of roots for the first 15 perfect squares
roots = [math.sqrt(i) for i in range(1, 16)]

def perform_operations(roots):
    print("Original List of Roots:")
    print(roots)

    # 1. Access link using positive indexing
    print("\nAccessing element at index 5 (positive indexing):", roots[5])

    # 2. Access link using negative indexing
    print("Accessing element at index -1 (negative indexing):", roots[-1])

    # 3. Delete the last element of the list
    print("\nDeleting the last element...")
    deleted_element = roots.pop()  # Remove and return the last element
    print("Deleted Element:", deleted_element)
    print("List after deletion:")
    print(roots)

    # 4. Add an element at the end of the list
    new_element = 4.5  # Example element to add
    roots.append(new_element)
    print("\nAdded Element:", new_element)
    print("List after addition:")
    print(roots)

    # 5. Repeat the list using operator
    repeated_roots = roots * 2
    print("\nRepeated List:")
    print(repeated_roots)

    # 6. Get middle element
    middle_index = len(roots) // 2
    middle_element = roots[middle_index]
    print("\nMiddle Element:", middle_element)

    # 7. Traverse the entire list
    print("\nTraversing the entire list:")
    for index, value in enumerate(roots):
        print(f"Index {index}: {value}")

# Execute the operations
perform_operations(roots)
