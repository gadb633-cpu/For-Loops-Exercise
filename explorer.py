# part 1
# 1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# 2
for list in range(1,6):
    print(list)
# 3
for list in range(0,10,2):
    print(list)
# 4
for fruit in enumerate(fruits):
    print(fruit)    
# 5
scores = {"alpha":80,"bravo":95}
item = scores.items()
for score in item:
    print(score)
# 6
numbers = [1,2,3,4,5]
sum = 0
for number in numbers:
    sum += number
print(sum)    
# 7
i = 1
while i <= 5:
    print(i)
    i += 1
for x in range(1,6):
    print(x)
# 8
matrix = [[1, 2, 3], [4, 5, 6]]
for x in matrix:
    for y in x:
        print(y)
# 9
numbers = [1,2,3,4,5,6,7,8,9,10]
squares_num = [x**2 for x in numbers]        
print(squares_num)
# 10
squares_num = [x for x in range(1,21) if x % 2 == 0]
print(squares_num)        
# part 2
# 1
names = ["Alpha", "Bravo"]
scores = [80,95]

for name in zip(names,scores):
    print(name)
