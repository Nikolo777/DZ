start = int(input("укажите кол-во км за 1-й день "))
goal = int(input("укажите желаемое кол-во км "))

scetcik = 1
while start < goal:
    scetcik += 1
    start += start * .10
else:
    print(f"вам потребуется на цель  {scetcik} дней")
