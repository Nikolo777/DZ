virucka = int(input("введите сумму выручки : "))
izderjki = int(input(" введите сумму издержек : "))
pribili = virucka - izderjki

if pribili:
    rentabelnost = pribili / virucka
    print(f"прибыль = {pribili}, ренатбельность = {rentabelnost} ")

    sotrudniki = int(input("укажите кол-во сотрудников : "))

    odinsotrudnik = pribili / sotrudniki
    print(f"прибыль на одного сотрудника = {odinsotrudnik}")

else:
    print(f"убыток равен: {pribili}")
