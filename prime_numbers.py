number = int(input("Enter the number : "))

prime_numbers = []
for n in range(2,number+1) :
    count  = 0
    for i in range (1,number) :
        if n % i == 0 :
            count += 1
    if count == 2 :
        prime_numbers.append(n)
print("The prime number list is", prime_numbers)