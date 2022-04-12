def sortare(limba):
    with open("Language.txt", "r") as textfile:
        file = textfile.readlines()
        for i in file:
            i = i.split()
            if (i[0] == limba):
                return i[1]
