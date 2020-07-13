counter = 0
number = input('Please enter a number :')

for i in range(2, int(number)):
    if (int(number)%i == 0):
        counter += 1
        break

if(counter!=0):
      print(number, "is not a prime number")
else:
      print(number, "is a prime number")