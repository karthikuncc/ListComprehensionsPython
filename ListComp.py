nums = [1,2,3,4,5,6,7,8,9,10]

#List Comprehensions
my_list = [n*n for n in nums]
my_list = [n for n in nums if n%2==0]
my_list = [ (letter,num) for letter in 'abcd' for num in range(4)]
my_list=[x for x in 'MATHEMATICS' if x in ['A','E','I','O','U']]
#Removing vowels
sentence = 'My name is Aarshay Jain!'
 vowels = 'aeiou'
result=''.join([ l for l in sentence if l not in vowels])
#Flatten Matrix
my_list=[x for row in matrix for x in row ]
my_list=[x+1 if x>=5 else x+5 for x in nums]

#String to Extracting digits of a number in to a list using LC
inp=12344
my_list=[int(d) for d in str(inp)]

#Elif can be avoided with the below style by if else
for v in nums:
    if v == 1 :
        print('yes')
    else:
        if v == 2:
            print('no')
        else:
            print('idle')
 #Elif can be avoided with the below style by if else Using LC
my_list=['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in nums]
for i in my_list:
    print(i)

#Break statements can not be used in LC
def oddNumbersBeforeZero(sequence):
    return sum([1 if n%2==1  elif n==0 break for n in sequence])
