def sort_expression(s):
    numbers = list(map(int, s.split("+")))
    numbers.sort()

    new_expression = "+".join(map(str, numbers))

    return new_expression


input_exp = input().strip()
sorted_exp = sort_expression(input_exp)
print(sorted_exp)

 
