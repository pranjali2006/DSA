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

"""#finding largest numbers
numbers=[-8,-3,-12,-1,-6]
max=numbers[0]
for i in numbers:
    if i > max:
        max=i
print(max)"""


"""#reversing the array (2pointers approach)
num=[1,2,3,4,5,6,7,8,9]
left=0
right=len(num)-1

while left < right :
    swap=num[left]
    num[left]=num[right]
    num[right]=swap

    left=left + 1
    right=right-1
    
print(num)
#time complexity=o(n)
#space:o(1)

"""

#array frequency counting using dictonary
"""num=[1,2,3,2,3,1,3,4,1,2,4,4,2,1]
freq={}

for i in num:
    if i in freq:
        freq[i]=freq[i] + 1
    else:
        freq[i]=1
print(freq)
"""
a=[1,2,3,16,2,2,2,2,66,66,66,10]
freq={}

for i in a:
    if i in freq:
        freq[i]=freq[i] + 1
    else:
        freq[i]=1
  
  
for key,value in freq.items():
    if value > 1:
        print("key :",key,"value :",value)