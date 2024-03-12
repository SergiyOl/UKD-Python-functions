def ToPow(a, b):
    if a == b:
        return "Числа однакові"
    elif a < b:
        temp = (a + b) / 2
        b = a * b * 2
        a = temp
        return a, b
    else:
        temp = (a + b) / 2
        a = a * b * 2
        b = temp
        return a, b

print(ToPow(float(input("Введіть число (a): ")), float(input("Введіть число (b): "))))