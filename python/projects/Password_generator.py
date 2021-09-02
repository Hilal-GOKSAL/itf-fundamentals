# Password Generators;
import random
# we will go with ASCII codes(with using ASCII table)

# ascii code
chr(68)

random.randint(1,10)            # Signature: random.randint(a, b)
random.randint(65,90)           # Docstring:
                                # Return random integer in range [a, b], including both end points.

chr(random.randint(65,90))

uppers = [chr(random.randint(65,90)) for i in range(3)]
print(uppers)                              # ['Y', 'W', 'A']
"".join(uppers)                     # 'YWA'


lowers = [chr(random.randint(97,122)) for i in range(3)]
print(lowers)                                 # ['m', 'v', 'u']

numbers = [chr(random.randint(48,57)) for i in range(3)]
print(numbers)                                # ['1', '8', '4']

special_char = chr(random.randint(33,47)) + chr(random.randint(58,64))
print(special_char)                           # '%;'


password = "".join(uppers) + "".join(lowers) + "".join(numbers) + "".join(special_char)
print(password)                        # 'YWAmvu184%;'

random.shuffle(uppers)
print(uppers)                          # ['W', 'Y', 'A']


def shuffleit(string):
    template_list = list(string)
    random.shuffle(template_list)
    return "".join(template_list)

pasw = shuffleit(password)
print(pasw)                     # new password option; '%YmA;W48v1u'    

