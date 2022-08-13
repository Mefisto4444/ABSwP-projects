def SPC(password):
    import re
    strongPasswordBlueprint = re.compile(r"""

    (?=.*\d.*\d)#.....................Przynajmniej 2 cyfry
    (?=.*[!@#$%^&*])#.............Przynajmniej jeden znak specjalny
    (?=.*[A-Z].*[A-Z])#.................Przynajmniej 2 duże litery
    (?=.*[a-z].*[a-z])#...............Przynajmniej 2 małe liter
    (.{8,})#.............Przynajmniej 8 znaków

    """,re.VERBOSE)
    moP = strongPasswordBlueprint.search(password)
    if moP == None:
        print("Hasło jest słabe")
        return False
    else:
        print("Hasło jest silne")
        return True
SPC(input(": "))