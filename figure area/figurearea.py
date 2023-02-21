x = str (input ())

if x == ("треугольник"):
    a = int(input())
    b = int(input ())
    c= int(input ())
    p = ((a + b + c) / 2)
    S = p*(p-a)*(p-b)*(p-c)
    print (math.sqrt(S))
else:
     print ("")
     if x==("прямоугольник"):
         a = int (input ())
         b = int (input ())
         S = a*b
         print (float (S))
     else:
         print ("")
         if x == ("круг"):
             r = int (input ())
             pi = 3.14
             S =  pi*(r**2)
             print (float (S))
         else:
             print ("")