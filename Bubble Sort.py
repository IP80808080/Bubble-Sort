
x = int(input("Enter the range of list:"))
l = []
for i in range(x):
    z = int(input("Enter the Element: "))
    l.append(z)
print("Old Sort",l)
for a in range(len(l)-1):
    for b in range(len(l)-1):
        if l[b] > l[b+1]:
            l[b], l[b+1] = l[b+1], l[b]

print("New Sort",l)
        
