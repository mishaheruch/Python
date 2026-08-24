def count_positive(numbers):
    total = 0
    for nums in numbers:
        if nums > 0:
            total += 1
    return total



print(count_positive([1, -2, 3, -4, 5]))
print(count_positive([-1, -2, -3]))