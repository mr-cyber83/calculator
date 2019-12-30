import math
def circle():
    r= input ("give me ray to caculate: ")
    r= float(r)
    pi= 3.141592653589793
    x= pi*r
    parameter= x*2
    print(parameter, "cm of the circle parameter")
def ethad_2jomlei_negetiv():
    A= input ("give me a: ")
    B= input ("give me b: ")
    A= float (A)
    B= float (B)
    a= A**2
    b= B*B
    C= (A*B)*2
    print (a,C,b)
    X= a-C+b
    print (X,"answer you requset")
    input("Please Enter To Exit....")
def ethad_mozdvj():
    A=input ("give me a: ")
    B=input ("give me b: ")
    a= float(A)
    b= float(B)
    A= a-b
    B= a+b
    x= A*B
    print(x, "aswer you requset")
def ethad_2jomlei_plus():
    A= input ("give me a: ")
    B= input ("give me b: ")
    A= float (A)
    B= float (B)
    a= A*A
    b= B*B
    C= (A*B)*2 
    print (a,C,b)
    X= a+b+C
    print(X, "answer you requset")
def mokab_2jomlei_negetiv():
    A= input ("give me a: ")
    B= input ("give me b: ")
    A= float (A)
    B= float (B)
    a= A*A*A
    b= -B*-B*-B
    c= ((A*A)*B)*-3
    d= ((B*B)*A)*3
    print (a,c,d,b)
    x=a+b+c+d
    print(x, "answer you requaset")
def mokab_2jomlei_plus():
    A= input ("give me a: ")
    B= input ("give me b: ")
    A= float (A)
    B= float (B)
    a= A*A*A
    b= B*B*B
    c= ((A*A)*B)*3
    d= ((B*B)*A)*3
    print (a,b,c,d)
    x=a+b+c+d
    print(x, "answer you requset")
def fisaqores():
    a = input ("give me a: ")
    b = input ("give me b: ")
    a = float(a)
    b = float(b)
    x = a*a
    z = b*b
    c = x+z
    c = float(c)
    x = c
    x = float(x)
    sr = math.sqrt(x)
    print(sr)
def fat_larg_negetiv():
    X= input ("give me x: ")
    Y= input ("give me Y: ")
    Y= float(Y)
    X= float(X)
    y= X-Y
    x= X*X
    a= X*Y
    b= Y*Y
    print (y,x,a,b)
    ab= x+a+b
    aswer= y*ab
    print(aswer)
def fat_larg_plus():
    X= input ("give me x: ")
    Y= input ("give me Y: ")
    Y= float(Y)
    X= float(X)
    y= X+Y
    x= X*X
    a= X*Y
    b= Y*Y
    print (y,x,-a,b)
    ab= x-a+b
    aswer= y*ab
    print(aswer)
def tak_jomlei_mshtrk():
    A= input("give me a: ")
    B= input("give me b: ")
    X= input("give me x: ")
    A= float(A)
    B= float(B)
    X= float(X)
    x= X*X
    a= A+B
    c= a*X
    b= A*B
    print (x,c,b)
    aswer= x+c+b
    print(aswer)
def sqrt():
    x=input ("give me X to calculate: ")
    x= float(x)
    x=math.sqrt(x)
    print (x)