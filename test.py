y = [1,45,66,22,1988]
x = 0

while ( x not in y ):
    print("X = ",x)
    x = random.randrange(0,1999)

print("X in y, X=", x)