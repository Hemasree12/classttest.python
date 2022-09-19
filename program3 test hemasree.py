n = int (input("Enter the number"))
factorial = 1
if n < 0:
         print ("factorial is not possible")
elif n == 0:
    print ("Factorial of the number is 1")

else:
    for i in range (1, n+1):
        factorial = factorial*i
        print("Factorial of the given number is:", factorial)
 

