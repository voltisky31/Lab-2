a = int(input("Wpisz liczbę a: "))
b = int(input("Wpisz liczbę b: "))
c = int(input("Wpisz liczbę c: "))
if (a == b == c):
    print("Te liczby są sobie równe")
elif (a > b and a > c):
    print("Liczba a jest największa")
elif (b > a and b > c):
    print("Liczba b jest największa")
elif (c > b and c > a):
    print("Liczba c jest największa")
elif (a == b and a > c):
    print("Liczby a oraz b są największe oraz sobie równe")
elif (b == c and b > a):
    print("Liczby b oraz c są największe oraz sobie równe")
elif (a == c and a > b):
    print("Liczby a oraz c są największe oraz sobie równe")