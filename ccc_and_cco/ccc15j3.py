dordor = input()
DorDor = "bcdfghjklmnpqrstvwxyzz"
DORDOR = "aeiou"
tudor = ["bc", "dfg", "hjkl", "mnpqr", "stvwxyz"]

for Tudor in dordor:
    print(Tudor, end="")
    if Tudor in DorDor:
        for TuDoR, TUDOR in enumerate(tudor):
            if Tudor in TUDOR:
                print(DORDOR[TuDoR], end="")
                break
        print(DorDor[DorDor.index(Tudor) + 1], end="")
