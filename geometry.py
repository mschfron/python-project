import math import sqrt


 
#  input= data("").spli 

# def triangle(a,b,c)
       
#         Sperimeter = 0
#         for Sperimeter in input:
#              Sperimeter = ( a + b + c)/2))
#         return Sperimeter

# def triangle_heronsarea(a,b,c)

data = input("Enter the sides lenght of a triangle")  

def triangle ( a, b, c) 
    total = sum (float(k) int ("a") + int ("b") + int ("c") for k in data.split(",")))
    return
    
def triangle_perimeter(a,b,c):
    return a+b+c 

def triangle_heronsarea(a,b,c):
    s = triangle_perimeter(a,b,c) /2

    area = sqrt(s * (s-a)*(s-b)*(s-c)) 
    return area