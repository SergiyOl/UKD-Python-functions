def CloserDot(cord1x, cord1y, cord2x, cord2y):
    dot1dist = (cord1x**2 + cord1y**2)**0.5
    dot2dist = (cord2x**2 + cord2y**2)**0.5
    if dot1dist == dot2dist:
        return "Обидві точки рівновіддалені від центру"
    if dot1dist < dot2dist:
        return "Перша точка знаходиться ближче до центру"
    else:
        return "Друга точка знаходиться ближче до центру"

print(CloserDot(float(input("Введіть число (Точка 1, X): ")), float(input("Введіть число (Точка 1, Y): ")), float(input("Введіть число (Точка 2, X): ")), float(input("Введіть число (Точка 2, Y): "))))