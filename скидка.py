print("Введите число")
n=int(input())
if n<1001:
    print(n)
elif n>1000 :
    n=n-n//100*30
    print(n)