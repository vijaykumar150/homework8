import random

def check(a,b):
        if a == 0:
            return 0
        x = b/a
        return x
    
a = random.randrange(5)
b = random.randint(1,20)

print(a,b)
x = int(check(a,b))
print(x)

inp=input('Enter the value of {}/{}:'.format(b,a))
if type(inp) != "int":
  print("wrong input passed, aborting!")
else:
  if inp == x:
          print(inp)
          print("CORRECT!")
  else:
      print("INCORRECT!")