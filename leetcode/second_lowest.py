def second_smallest(numbers):
    smallest, sec_smallest = float('inf'), float('inf')
    for i in numbers:
        if i <= smallest:
            smallest, sec_smallest = i, smallest
        elif i < sec_smallest:
            sec_smallest = i
    return sec_smallest


lst = [10, 22, 34, 22, 21]
print(second_smallest(lst))
