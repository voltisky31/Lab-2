jestem_zbyt_leniwy_na_if = 1  #Za dużo warunków do napisania
if(jestem_zbyt_leniwy_na_if == 1):
    tab = []
    tab.append(int(input("Wpisz liczbę a: ")))
    tab.append(int(input("Wpisz liczbę b: ")))
    tab.append(int(input("Wpisz liczbę c: ")))
    tab.append(int(input("Wpisz liczbę d: ")))
    tab.sort()
    print("Największa wpisana liczba to:", tab[3])
