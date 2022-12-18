lst = []

    with open("Kombinationen.csv") as file:
        for line in file:
            zeile = line.strip().split(",")
            lst.append(zeile)
            
            
    print(lst)
