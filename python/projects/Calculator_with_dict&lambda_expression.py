# Building a Calculator using Dict with Lambda Expression

# (lambda x,y: x + y)(4,5)

ops = {"+":(lambda x, y : x + y), 
       "-":(lambda x, y : x - y), 
       "/":(lambda x, y : x / y), 
       "*":(lambda x, y : x * y)}
ops["+"](3,5)