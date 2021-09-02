# Comparison of for loops versus list comprehension in terms of speed

from timeit import timeit

def for_loop():
    result = []
    
    for i in range(1000000):
        result.append(i)
    return result


def list_comprehension():
    return[i for i in range(1000000)]


# Signature:
# timeit(
#     stmt='pass',
#     setup='pass',
#     timer=<built-in function perf_counter>,
#     number=1000000,
#     globals=None,
# )
# Docstring: Convenience function to create Timer object and call timeit method.
# Type:      function

time1= timeit(for_loop, number=1000)
time2 = timeit(list_comprehension, number=1000)
print(time1)                #169.47996750000016
print(time2)                # 116.99444249999988

print(f'List Comprehension is {round(time1/time2, 2)} times faster than for_loop.')
# List Comprehension is 1.45 times faster than for_loop.