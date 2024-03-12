def ToHigher(a, b):
    if a == b:
        a = 0
        b = 0
        return a, b
    
    if a < b:
        a = b
    else:
        b = a 
    return a, b

print(ToHigher(float(input("Введіть число (a): ")), float(input("Введіть число (b): "))))