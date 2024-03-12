def FindSection(cordX, cordY):
    if cordX == 0 and cordY == 0:
        return "Знаходиться в центрі"
    
    if cordX == 0:
        partX = "На осі Y"
    elif cordX < 0:
        partX = "-X"
    else:
        partX = "+X"
    
    if cordY == 0:
        partY = "На осі X"
    elif cordY < 0:
        partY = "-Y"
    else:
        partY = "+Y"
        
    return "Знаходиться в площі: " + partX + ", " + partY

print(FindSection(float(input("Введіть число (X): ")), float(input("Введіть число (Y): "))))