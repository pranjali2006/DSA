""" numbers=[12,5,20,8,15]
largest=numbers[0]
second_largest=None

for i in numbers:
    if i > largest:
        
        second_largest=largest
        largest=i
    elif i < largest and (
        second_largest is None or i > second_largest):
        second_largest=i

print("lagrest :",largest)
print("second :",second_largest)
"""


"""#2.ex how many elemetns are greeater than 10
numbers=[4,15,8,22,11,3,17]

count=0

for i in numbers:
    if i > 10:
        count=count + 1
print(count)"""

"""# first occurence of a number
numbers=[4,15,8,22,15,3,17]

target=15
for i in range(len(numbers)):
    if numbers[i]==target:
        print(i)
        break
else:
    print(-1)
"""

#finding largest numbers
numbers=[-8,-3,-12,-1,-6]
max=numbers[0]
for i in numbers:
    if i > max:
        max=i
print(max)