
def multiplicar(*args):
    total = 1
    for num in args:
        total *= num
    return total

m = multiplicar(1,2,3,4,5,6)

print(m)