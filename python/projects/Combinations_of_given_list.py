# Given a list such '[1,2,3]' get an all possible output combinations
# Output:

# [
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
# ]

# solution_0 = [[]]
# solution_1 = [[1], [2], [3]]
# solution_2 = [[1,2], [1,3], [2,1], [2,3], [3,1], [3,2]]
# solution_3 = [[1,2,3],[1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]  --> expected final result

# things we will use to solve this question: set(), list()-[], for loop

for index in range(len(num)):
    solution = [i + [j] for i in solution for j in num_set.difference(set(i))]
    print(solution)

# [[1], [2], [3]]
# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]