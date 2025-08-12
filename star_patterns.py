#This is the first pattern
n = int(input("Enter your number: "))
product = 1
for i in range(1, n+1):
    product = product*i
  
#This is the second pattern 
#I used end argument
n = int(input("Enter your number: "))
for i in range(1,n+1):
     print(" "*(n-i), end="")
     print("*"*(2*i-1) , end="")
     print("")

#This is the third pattern 
'''
 for n = 3
  ***
  * *
  ***
'''
n = int(input("Enter your number: "))
for i in range(1, n+1):
    if (i == 1 or i == n) :
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")

#This is the fourth pattern I learned, The Diamond shape
n = int(input("Enter number of rows: "))

# Upper part
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
