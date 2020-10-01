n = int(input("введите кол-во секунд"))
h = str(n // 3600)
m = (n // 60) % 60
s = n % 60
if m < 10:
    m = '0' + str(m)
else:
    m = str(m)
if s < 10:
    s = '0' + str(s)
else:
    s = str(s)
print(h + ':' + m + ':' + s)
