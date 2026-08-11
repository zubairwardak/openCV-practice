n = int(input("Enter a number: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(f"Factorial of {n} is {factorial(n)}")
    

# a = input("Enter a numbers: ")

# reverse = a[: : -1]
# print(reverse)

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
