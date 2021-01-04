a = float(input("Wpisz zawartość alkoholu w wydychanym powietru w mg/dm^3: "))
if (a < 0.1):
    print("Trzeźwy")
elif (0.1 <= a < 0.25):
    print("Po spożyciu %")
else:
    print("Nietrzeźwy")