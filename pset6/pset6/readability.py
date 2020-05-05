
text = input("Text: ")

L = 0
W = 0
S = 0

n = len(text)
if text[0] >= 'A' and text[0] <= 'z':
    W += 1
    
for i in range(n):
    if text[i] >= 'A' and text[i] <= 'z':
        L += 1
    if text[i] == ' ':
        W += 1
    if text[i] == '.' or text[i] == '!' or text[i] == '?':
        S += 1
g = round(0.0588 * (100 * L/W) - 0.296 * (100 * S/W) - 15.8)

if g < 1:
    print("Before Grade 1")
elif g <= 16:
    print(f"Grades: {g}")
else:
    print("Grades: grade 16+")
    