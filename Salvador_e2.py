# filename: Salvador_e2.py
# author: Ronald Salvador 
# description: This is a python program that classifies a tropical cyclone wrt its sustain winds


import sys

sustained_winds = sys.argv[1]

sustained_winds = float(sustained_winds)

if sustained_winds >= 220.0:
    print("Super Typhoon")
elif sustained_winds >= 188.0:
    print("Typhoon lang")
elif sustained_winds >= 89.0:
    print("Severe Tropical Storm")
elif sustained_winds >= 62.0:
    print("Tropical Storm")
else:
    print("yehey Tropical Depression lang ")