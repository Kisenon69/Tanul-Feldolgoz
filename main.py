tanulok = []

while True:
    print("\nKérem a tanuló adatait.")
    nev=input("Tanuló neve: ")
    szid=input("Születési idő: ")
    magassag = int(input("Magasság: "))

    tanulo = (nev, szid, magassag)
    tanulok.append(tanulo)

    valasz=input("További tanuló (igen/nem): ")
    if valasz.lower() is "igen":
        break

#3 feldolgozás lista alias elem (iten) segítségével
for item in tanulok:
    print(f"Tanuló neve: {item[0]}, születési ideje: {item[1]}, magassag: {item[2]}")