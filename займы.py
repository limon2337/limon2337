s=int(input("Руб"))
n=int(input("Лет"))
p=int(input("Проценты"))
r=p/100
m=(s * r * (1 + r)*n) / (12 * ((1 + r)*n - 1 ))
print("m","=", m)