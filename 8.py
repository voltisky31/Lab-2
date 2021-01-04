a = int(input("Podaj długość boku a: "))
b = int(input("Podaj długość boku b: "))
c = int(input("Podaj długość boku c: "))
if ((a*a) + (b*b) == (c*c) or (b*b) + (c*c) == (a*a) or (c*c) + (a*a) == (b*b)):
    print("Ten trójkąt jest prostokątny")
else:
    print("Ten trójkąt nie jest prostokątny")
