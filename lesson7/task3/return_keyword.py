def sum_two_numbers(a, b):
    return a + b

c = sum_two_numbers(3, 12)
print(c)

def fib(n):
    result = []
    a = 1
    b = 1
    while a < n:
        tmp_var = b
        b = a + b
        a = tmp_var
        result.append(a)
    return result

print(fib(100))
