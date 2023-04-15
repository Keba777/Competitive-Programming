def maxLength(n, a):
    max_length = 1
    current_length = 1

    for i in range(1, n):
        if a[i] >= a[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)


# Reading input and converting to the required format
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Finding the length of the maximum non-decreasing subsegment
result = maxLength(n, a)

# Printing the result
print(result)
