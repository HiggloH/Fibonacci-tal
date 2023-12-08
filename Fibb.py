from terminaltables import SingleTable

running = True

talen = []
header = []


def generera_tal(antal):
    # Formeln för sekvensen: Talen[n] = Talen[n-1] + Talen[n-2]

    # Range(2, antal tal) är för att inte starta på index 0 i talen listan
    for n in range(antal):
        if n == 0:
            talen.append(0)
        elif n == 1:
            talen.append(1)
        else:
            nya_talet = talen[n - 1] + talen[n - 2]
            talen.append(nya_talet)

        header.append('F:{0}'.format(n))

    # Lägg in huvudet och talen till en lista tillsammans
    table_data = [
        header,
        talen
    ]

    # Skapa en tabell med terminaltables
    table = SingleTable(table_data)
    table.inner_row_border = False
    print(table.table)


def start():
    try:
        antal_tal = int(input("Hur lång vill du att sekvensen ska vara? "))

        generera_tal(antal_tal)
    except ValueError:
        print("Inputen var ej endast ett tal")

        start()


while running:
    start()

    if str(input("Vill du avsluta? ")) == "ja":
        running = False
    else:
        # Återställ dessa listor för att inte förstöra sekvensen och huvudet till tabellen
        talen = []
        header = []
