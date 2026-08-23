
# Source - https://stackoverflow.com/a/39303880
# Posted by Karin, modified by community. See post 'Timeline' for change history
# Retrieved 2026-08-11, License - CC BY-SA 3.0

def vowels_count(s):
    i = 0
    counter = 0
    while i < len(s):
        if s[i] in 'aeiou':
            counter += 1
        i += 1
    return counter


# arr = [1, 2, 3, 4, 5]

# largestv = arr[0]
# for i in arr:
#     if i > largestv:
#         largestv = i

# print(f"Largest value in the array is {largestv}")


# n = int(input("Enter a number: "))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(f"Factorial of {n} is {factorial(n)}")
    

# a = input("Enter a numbers: ")

# reverse = a[: : -1]
# print(reverse)

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
