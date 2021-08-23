# Armstrong Numbers- Assignment
# th powers of their digits (a finite sequence) are called Armstrong numbers or plus perfect number and are given by 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208 etc.
def is_armstrong():
    while True:
        num = input('Please enter a positive number: ')             # this is a string
        exponential = len(num)                                      # len can only use with string. It must be a string forever.
        total = 0                                                   # the box where I keep my total.


        if not num.isdigit():                                       # .isdigit for strings to check whether it has numeric value./ checking validity of my input.
            print(num, 'is invalid input. Please enter a positive number.')

        elif int(num) >= 0:                                        # we are converting num into integer to make sure that it is a positive integer.(absolute number)
            for i in range(exponential):                           # range(digit number) it will start from 0 and stops at the number of last digit of the given number(eg. num = '12345678' range(8)))
                total +=int(num[i]) ** exponential                 # filling up my total
            if total == int(num):                                  # we are converting varaible according to our demans, we are not assigning it to a new varaible.
                print(num, 'is an  Armstrong number! ')
                break                                              # stopping my loop
            else:
                print(num, 'is not an Armstrong number!')
                break                                              # stopping my loop
# Note: 0 to 9 is an Armstrong number. 

is_armstrong()