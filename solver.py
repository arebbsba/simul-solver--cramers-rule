eq_1 = input("Enter the first equation: format ax + by = c: ")
eq_2 = input("Enter the second equation: format dx + ey = f: ")

eq_1 = eq_1.replace(" ", "").replace("=", "+").split("+")
eq_2 = eq_2.replace(" ", "").replace("=", "+").split("+")

a, b, c, d, e, f = int(eq_1[0][:-1]), int(eq_1[1][:-1]), int(eq_1[2]), int(eq_2[0][:-1]), int(eq_2[1][:-1]), int(eq_2[2])

det = a*e - b*d
x = (c*e - b*f) / det
y = (a*f - c*d) / det

print(f"x = {x}, y = {y}")