from cs50 import get_int

h = get_int("Height: ")

while h <= 0 or h >= 9: 
    h = get_int("Height: ")

for i in range(h):
    print(" " * (h-1-i), end="")
    print("#" * (i+1)) 
    