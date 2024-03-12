def FindNegative(a, b, c):
    arr = [a, b, c]
    counter = 0
    for i in arr:
        if i < 0:
            counter +=1 
    return counter

print(FindNegative(float(input("Введіть число (a): ")), float(input("Введіть число (b): ")), float(input("Введіть число (c): "))))