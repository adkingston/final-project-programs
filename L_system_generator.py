import turtle
import re



def replace(repls,string):
    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                  lambda k: repls[k.group(0)], string)

def instructions(str1, Ato, Bto, level): 
    for i in range(level):
        str1 = replace({'A': Ato,'B': Bto},str1)
    if "F" in str1:
        str2 = str1.translate(None,"A").translate(None,"B")  
    else:
        str2 = str1.replace('A','F').replace('B','F')
    return str2
      
    
def drawLsystem(instructions, angle, distance):
    for cmd in instructions:
        if cmd == "F":
            turtle.forward(distance)
        elif cmd == "+" :
            turtle.right(angle)
        elif cmd == "-":
            turtle.left(angle)

wn = turtle.Screen()
turtle.hideturtle()
turtle.speed('fastest')

#I will generate a dictionary of possible curves for the program above to draw

def peano_gosper(d, level):
    A = "A-B--B+A++AA+B-"
    B = "+A-BB--B-A++A+B"
    inst = instructions('A', A, B, level)
    drawLsystem(inst, 60, d)
    wn.exitonclick()    
    
def sierpinski_triangle(d, level):
    A = "B-A-B"
    B = "A+B+A"
    inst = instructions('A', A, B, level)
    drawLsystem(inst, 60, d)
    wn.exitonclick()  

def triangle(d,level):
    A = "A+A-A-A+A"
    B = ""
    inst = instructions('A', A, B, level)
    drawLsystem(inst, 90, d)
    wn.exitonclick()
    
def carpet(d,level):
    A = "A+A-A-A-B+A+A+A-A"
    B = "BBB"
    inst = instructions('A', A, B, level)
    drawLsystem(inst, 90, d)
    wn.exitonclick() 
    
def dragon(d,level):
    A = "A-A+A"
    B = ""
    inst = instructions('A', A, B, level)   
    drawLsystem(inst, 120, d)
    wn.exitonclick()

def hilbert(d,level):
    A = "+BF-AFA-FB+"    
    B = "-AF+BFB+FA-"
    inst = instructions('A', A, B, level)   
    drawLsystem(inst, 90, d)
    wn.exitonclick()

def peano(d,level):
    A = "AFBFA+F+BFAFB-F-AFBFA"
    B = "BFAFB-F-AFBFA+F+BFAFB"
    inst = instructions('A', A, B, level)
    drawLsystem(inst, 90, d)
    wn.exitonclick()
    
def trapazoid(d, level): #needs fixing
    A = '-A-A++A---'
    B = ''
    inst = instructions('A',A,B,level)
    drawLsystem(inst, 60, d)
    wn.exitonclick()

peano(10,2)
    
turtle.delay()
turtle.done()


