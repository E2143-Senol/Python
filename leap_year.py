leap_year = int(input("Yılı giriniz. Örn : 2000"))

if leap_year % 400 == 0:
    print(leap_year, "is a leap year")
elif leap_year % 100 == 0:
    print(leap_year, "is not a leap year")
elif leap_year % 4 == 0:
    print(leap_year, "is a leap year")
else:
    print(leap_year, "is not a leap year")