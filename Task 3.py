def Triangle(a, b):
    a = abs(a)%360
    b = abs(b)%360
    if a + b > 360:
        return "Такий трикутник неможливий"
    c = 360 - a - b
    if a == 90 or b == 90 or c == 90:
        return "Кут с дорівнює: " + str(c) + ", трикутник є прямокутним"
    else:
        return "Кут с дорівнює: " + str(c)

print(Triangle(int(input("Введіть число (кут a): ")), int(input("Введіть число (кут b): "))))