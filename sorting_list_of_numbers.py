list = [5, 2, 8, 1, 9, 3]

# Sorting the list in ascending order
while True:
    swapped = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            # Swap the elements
            list[i], list[i + 1] = list[i + 1], list[i]
            swapped = True
    if not swapped:
        break

print("Sorted list:", list)