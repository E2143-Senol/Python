number = input("Armstrong number check. Please enter a positive integer number")

while type(eval(number)) == float or number.isalpha() or type(eval(number)) == bool or int(number) < 0  :
   print(number, "It is an invalid entry. Don't use non-numeric, float, or negative values!")
   number = input("Armstrong number check. Please enter a positive integer number")

number_list = list(str(number))
sum = 0
basamak_sayisi = len(number_list)
print(number_list)
for i in range(basamak_sayisi):
    basamak = int(number_list[i])**basamak_sayisi
    sum += basamak
    print(sum)

if sum == int(number) :
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")