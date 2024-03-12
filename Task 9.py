def IsWholeNum(a, b, c):
    arr = [a, b, c]
    counter = 0
    for i in arr:
        if i == int(i):
            counter +=1 
    return counter

print(IsWholeNum(float(input("Введіть число (a): ")), float(input("Введіть число (b): ")), float(input("Введіть число (c): "))))