# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 18:51:10 2016

@author: Alexander
"""
"""This program takes in a binary number as a string and returns the equivalent quartenary and its location in the unit square"""

import turtle
import random


def spacefillingfunction(L):
    M = (int(max(L))) #guess the type of enerary 
    
    if M >= 3 or len(L) % 2 != 0:
        return "StringError"
    
    else:
        L1 = [L[i:i+2] for i in range(0,len(L),2)] #group the digits into pairs and add them to a list
        
        L2 = [str((M+1)*int(i[0])+int(i[1])) for i in L1] #put each pair through the function 
                                                        #b1b2 = (2xb1+b2)
        L3 = "".join(L2) #put the result back into a single string
        
        if len(L) % 2 != 0: #again, consider the possibility of an odd number of digits. 
            L4 = "".join([L3[:-2],str(int(L3[-2])+1)]) #if odd, then do the reverse of the above
        else:
            L4 = L3
            
        return "".join(L4)


turtle.hideturtle()
turtle.speed("fastest")
    
def draw_4x4_grid(s):  #simple program draws 4 squares to make a grid
    
    for i in range(4):      #first quadrant
        turtle.forward(s)
        turtle.left(90)
    turtle.penup()
    turtle.forward(s)
    turtle.pendown()
    
    for i in range(4):      #second quadrant
        turtle.forward(s)
        turtle.left(90)
    turtle.penup()
    turtle.left(90)
    turtle.forward(s)
    turtle.right(90)
    turtle.pendown()
    
    for i in range(4):      #third quadrant
        turtle.forward(s)
        turtle.left(90)
    turtle.penup()
    turtle.backward(s)
    turtle.pendown()
    
    for i in range(4):      #fourth quadrant
        turtle.forward(s)
        turtle.left(90)
    turtle.right(90)
    turtle.forward(s)
    turtle.left(90)


def binary_to_point(s,L):
    draw_4x4_grid(s)
    k = spacefillingfunction(L)  #convert the binary to a quartenary  

    for j in range(len(k)):     
        if k[j] == '0':            #determine where to go for a 0 value and repeat at half the scale
            if j == len(k)-1:   #repeat for all possible values
                turtle.begin_fill()
            draw_4x4_grid(s/2**(j+1))
            if j == len(k)-1:
                turtle.end_fill()
            
        elif k[j] == '1':          
            turtle.penup()
            turtle.left(90)
            turtle.forward(s/2**(j))
            turtle.right(90)
            turtle.pendown()
            if j == len(k)-1:
                turtle.begin_fill()
            draw_4x4_grid(s/2**(j+1))
            if j == len(k)-1:
                turtle.end_fill()
            
        if k[j] == '2':
            turtle.penup()
            turtle.forward(s/2**j)
            turtle.left(90)
            turtle.forward(s/2**j)
            turtle.right(90)
            turtle.pendown()
            if j == len(k)-1:
                turtle.begin_fill()
            draw_4x4_grid(s/2**(j+1))
            if j == len(k)-1:
                turtle.end_fill()
            
        if k[j] == '3':
            turtle.penup()
            turtle.forward(s/2**j)
            turtle.pendown()
            if j == len(k)-1:
                turtle.begin_fill()
            draw_4x4_grid(s/2**(j+1))
            if j == len(k)-1:
                turtle.end_fill()
    turtle.delay()
    turtle.done()

def random_binary(C):
    R = []    
    for i in range(C):
        R.append(str(random.randint(0,1)))
    S = "".join(R)
    return S

#example
X = random_binary(10)
print binary_to_point(150,X)
