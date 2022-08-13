samogłoski = ["a", "e", "i", "o", "u", "y"]
text = input("Podaj text, który będzie przekonwertowany na świńską łacinę: ")
textList = text.split()
łacina = ""
duża = False
for i in range(len(textList)):
    if textList[i][0].lower() in samogłoski:
        textList[i] = textList[i] + "way"
    elif textList[i][0] not in samogłoski and textList[i].isalpha():
        if textList[i][0].isupper() == True:
            duża = True
        if duża == True:
            textList[i] = textList[i][1].upper() + textList[i][2:] + textList[i][0].lower() + "ay"  
        else:
            textList[i] = textList[i] + textList[i][0].lower() + "ay"        
            textList[i] = textList[i][1:]
    duża = False

    
łacina = " ".join(textList)
print(łacina)
