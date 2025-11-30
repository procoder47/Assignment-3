
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
user = int(input("Enter a number: "))
print(f"Factorial of 5 is : {factorial(user)}")

