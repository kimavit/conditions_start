n = int (input ())
if ((n%100)//10)==1:
     print ( str (n) + " программистов")
elif n%10 == 0 or n%10 == 5 or n%10==6 or n%10==7 or n%10==8 or n%10==9:
     print (str (n) + " программистов")
elif n%10 == 1:
     print (str (n) +  " программист")
elif n%10 == 2 or n%10 == 3 or n%10 == 4:
     print (str (n) +  " программиста")
else:
     print ("")