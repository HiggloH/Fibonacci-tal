from terminaltables import SingleTable

running = True

# Eftersom sekvensen alltid startar på 0 och 1
talen = [0, 1]
header = ["F:0", "F:1"]


def generera_tal(antal):
    # Formeln för sekvensen: Talen[n] = Talen[n-1] + Talen[n-2]

    # Range(2, antal tal) är för att inte starta på index 0 i talen listan
    for n in range(2, antal):
        nya_talet = talen[n - 1] + talen[n - 2]
        talen.append(nya_talet)

        header.append('F:{0}'.format(n))

    table_data = [
        header,
        talen
    ]

    table = SingleTable(table_data)
    table.inner_row_border = False
    print(table.table)


def start():
    antal_tal = int(input("Hur lång vill du att sekvensen ska vara? "))

    generera_tal(antal_tal)


while running:
    start()

    if str(input("Vill du avsluta? ")) == "ja":
        running = False
    else:
        # Återställ dessa listor för att inte börja upprepa dom vid flera generationer efter varandra
        talen = [0, 1]
        header = ["F:0", "F:1"]
