# Task: 
    # How many same numbers are there in the list? 
def equal(a,b,c): 
    numbers = [a,b,c]    # we can also use list function in here.
    result = numbers.count(max(numbers, key = numbers.count))
    
    if result > 1:
        return result
    else:
        return 0

equal(1,4,4)  # 2
equal(1,1,1)  # 3
equal(1,2,3)  # 0

# with arbitrary numbers of arguments
def equal_2(* arg): 
    numbers = list(arg)    # we can also use list function in here.
    result = numbers.count(max(numbers, key = numbers.count))
    
    if result > 1:
        return result
    else:
        return 0

equal_2(1,2,2,2,4)  # 3


# solution with Lambda expression:
# res if res > 1 else 0
# body_if if condition else body_else
equal = lambda a,b,c : [a,b,c].count(max([a,b,c], key = [a,b,c].count)) if [a,b,c].count(max([a,b,c], key = [a,b,c].count)) > 1 else 0


# lambda with arbitrary numbers of arguments:
 
# with back-slash "\" you can  move to the second line
equal_lambda_args = lambda * x : list(x).count(max(list(x), key = list(x).count))\
if list(x).count(max(list(x), key = list(x).count)) > 1 else 0

equal_lambda_args(1,2,2,2,4)  # 3