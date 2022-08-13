

def ReStrip(string, chars = None):
    import re
    if chars == None:

        LeftStrip = re.compile(r"^\s*")
        RightStrip = re.compile(r"\s*$")
    else:
        LeftStrip = re.compile(r"^[" + re.escape(chars) + r"]*")
        RightStrip = re.compile(r"[" + re.escape(chars) + r"]*$")
    string = re.sub(LeftStrip, "", string)
    string = re.sub(RightStrip, "", string)
    return string


print(ReStrip(input("Ciąg znaków: "), input("Znaki do usunięcia: ")))