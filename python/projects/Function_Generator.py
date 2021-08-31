# Taks: Create a function generator named as: function_generator()
# Example:
        # myPrint() = function_generator(print)

        # myMax() = function_generator(max)

        # myBool() = function_generator(bool)

        # mySorted() = function_generator(sorted)
# Mere lambda expressions will be;
    # (lambda x: print(x))("Write me down")  ==> Write me down
    # (lambda x: max(x))([1,2,34])           ==> 34
    # (lambda x: bool(x))("Write me down")   ==> True

def function_generator(function):
    return lambda x: function(x)

myPrint = function_generator(print)
myPrint("You can write whatever you want! ")
        # You can write whatever you want! 
myBool = function_generator(bool)
myBool("")
        # False