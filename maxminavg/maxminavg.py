a = int(input ())
b = int(input ())
c = int(input ())

if a <= b <= c:
    print(c, a, b, sep='\n')
elif b <= c <= a:
    print(a, b, c, sep='\n')
elif c <= a <= b:
    print(b, c, a, sep='\n')
elif a <= c <= b:
    print(b, a, c, sep='\n')
elif b <= a <= c:
    print(c, b, a, sep='\n')
elif c <= b <= a:
    print(a, c, b, sep='\n')
else:
    print ('')