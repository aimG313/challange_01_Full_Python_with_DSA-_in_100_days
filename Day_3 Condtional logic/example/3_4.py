a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if(a>b and a>c and a>d):
  print(a,"is largest")
elif(b>a and b>c and b>d):
  print(b,"is largest")
elif(c>a and b<c and c>d):
  print(c,"is largest")
else:
  print(d,"is largest")