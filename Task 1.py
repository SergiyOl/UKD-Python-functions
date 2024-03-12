def ToPow(a, b, c):
    arr = [a, b, c]
    j = []
    for i in arr:
        if i < 0:
            j.append(i**4) 
        else:
            j.append(i**2)
    return j

print(ToPow(float(input("Введіть число (a): ")), float(input("Введіть число (b): ")), float(input("Введіть число (c): "))))