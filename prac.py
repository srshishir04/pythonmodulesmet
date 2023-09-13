myTuples = (1,4,5)
print(myTuples)
print(myTuples[1:])
myTuples2=(1,)
print(myTuples2)
point = (2,3)
x,y = point
print(x)
grades = (5,2,6,4,8)
total = 0
for grade in grades:
    total +=grade
print(f"the total is {total}")
avg = total / len(grades)
print(f"Here is the average {avg}")