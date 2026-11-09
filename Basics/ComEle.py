# Common Elements Using Sets: Given two lists:
 
    ```python
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    ```


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

# Common elements
print("Common elements:", set1 & set2)

# Elements only in first list
print("Only in first list:", set1 - set2)

# All unique elements
print("All unique elements:", set1 | set2)    
