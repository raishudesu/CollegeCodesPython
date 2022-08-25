from cmath import sqrt

def pytha():
    user = int(input("Press 1 for a, 2 for b, 3 for c: "))
    
    def asqrd():
        b = int(input("What is the b? "))
        c = int(input("What is the c? "))
        formula = c**2 - b**2
        ans = sqrt(formula)
        print(ans)

    def bsqrd():
        a = int(input("What is the a? "))
        c = int(input("What is the c? "))
        formula = c**2 - a**2
        ans = sqrt(formula)
        print(ans)

    def csqrd():
        a = int(input("What is the a? "))
        b = int(input("What is the b? "))
        formula = a**2 + b**2
        ans = sqrt(formula)
        print(ans)

    if user==1:
        asqrd()

    elif user==2:
        bsqrd()

    elif user==3:
        csqrd()

pytha()



