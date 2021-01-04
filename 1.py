a = int(input("Wpisz liczbę a: "))
b = int(input("Wpisz liczbę b: "))
if (b == 0):
    print("Nie dzielimy przez zero")
elif(a % b == 0):
    print("A jest podzielne przez B")
else:
    print("A nie jest podzielne przez B")