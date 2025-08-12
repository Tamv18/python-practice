def greet(name, ending):
    print("Hello, " + name)
    print(ending)
    return "ok"
a = greet("Tam", "Thankyou")
print(a)

def factorial(n):
    if (n == 1 or n == 0):
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number:"))
print(f"The factorial of this number is {factorial(n)} ")

a = 7
b = 2
c = 3
def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
print(greatest(a, b, c))

def c_to_f(f):
    return 5*(f-32)/9
f = int(input("Enter your temperature: "))
c = c_to_f(f)
print(f"{round(c,2)}°C")

def sum(n):
    if (n == 1):
        return 1
    return sum(n-1) + n
n = int(input("Enter your number: "))
print(f"The sum of first n natural numbers is {sum(n-1) +n}.")


def pattern(n):
    if (n==0):
        return
    print("*"*n)
    pattern(n-1)
pattern(3)

def in_cm(cm):
    return a*2.54
a = int(input(" Enter your number: "))
print(f"{in_cm(a)}cm")
