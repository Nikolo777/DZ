n = int(input("введите любое число"))
ls = []
while n > 10:
    ls.append(n % 10)
    n //= 10
r = max(ls)
print("самая большая цифра в это числе: ")
print(r)
