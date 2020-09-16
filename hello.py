def willIMakeIt(distance, gasleft, mpg = 25):
    return gasleft * mpg >= distance

print(willIMakeIt(50,2))
print(willIMakeIt(100,1,50))
