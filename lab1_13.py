#13. Дані координати двох протилежних вершин прямокутника: (x1, y1), (x2, y2).
#Сторони прямокутника паралельні до осів координат. Знайти периметр і площу даного прямокутника.
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
AB = abs(x2-x1)
BC = abs(y2-y1)
p = 2*(AB+BC)
S=AB*BC
print("P: ",p,",","S: ",S)

print("             ")

