b = False
a = int(input())
g = 0
i = 0
while a != 0:
    g += a
    i +=1
    if g == 10:
        b = True
        break
    a = int(input()) 
if b:
    print(i)
		
		
		
