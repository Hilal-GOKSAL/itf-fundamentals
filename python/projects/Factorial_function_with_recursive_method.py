# Let's define our own Factorial Function using Recursive Method

# def my_factorial(n):
#     result = 1
#     for i in range (1, n+1):
#         result *= i
#     return result

#     my_factorial(4)
    
    
    
# with recursive method:
    
def my_facto(n):
    if (n ==1) or n==0:
        return  1
    else:
        return n * my_facto(n-1)
    my_facto(0)