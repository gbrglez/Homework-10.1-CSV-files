with open("seznam.txt", "r") as seznamFile:
    seznam = seznamFile.read().splitlines()
    for row in seznam:
        column = row.split(",")
        print(column[0]+" is "+column[1]+" years old and "+column[2])
