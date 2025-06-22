| Method      | Description                                                     | Sample Usage                                              |
| ----------- | --------------------------------------------------------------- | --------------------------------------------------------- |
| `append()`  | Adds a single item to the end of the list.                      | `lst.append(4)` → `[3, 1, 2, 4]`                          |
| `extend()`  | Adds all elements of an iterable to the end.                    | `lst.extend([5, 6])` → `[3, 1, 2, 4, 5, 6]`               |
| `insert()`  | Inserts an item at a specific index.                            | `lst.insert(1, 10)` → `[3, 10, 1, 2, 4, 5, 6]`            |
| `remove()`  | Removes the first matching element.                             | `lst.remove(10)` → `[3, 1, 2, 4, 5, 6]`                   |
| `pop()`     | Removes and returns the item at the given index (default last). | `lst.pop()` → removes `6`, list becomes `[3, 1, 2, 4, 5]` |
| `index()`   | Returns the index of the first matching value.                  | `lst.index(4)` → `3`                                      |
| `count()`   | Returns the count of the value.                                 | `lst.count(2)` → `1`                                      |
| `sort()`    | Sorts the list in ascending order (in-place).                   | `lst.sort()` → `[1, 2, 3, 4, 5]`                          |
| `reverse()` | Reverses the list in-place.                                     | `lst.reverse()` → `[5, 4, 3, 2, 1]`                       |
| `copy()`    | Returns a shallow copy of the list.                             | `copy_lst = lst.copy()` → `[5, 4, 3, 2, 1]`               |
| `clear()`   | Removes all items from the list.                                | `lst.clear()` → `[]`                                      |
