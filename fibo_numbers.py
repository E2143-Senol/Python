n0 = 1
n1 = 1
fibo_numbers = [n0, n1]
max = 0
while max < 55:
    max = n0 + n1
    fibo_numbers.append(max)
    n0 = n1
    n1 = max
    print(fibo_numbers)