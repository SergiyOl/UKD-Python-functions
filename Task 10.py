def IsWholeNum(a, b, c, k):
    arr = [a, b, c]
    counter = 0
    for i in arr:
        if i%k == 0:
            counter +=1 
    return counter

print(IsWholeNum(float(input("Введіть число (a): ")), float(input("Введіть число (b): ")), float(input("Введіть число (c): ")), float(input("Введіть дільник (k): "))))