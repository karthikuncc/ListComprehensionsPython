nums = [1,2,3,4,5,6,7,8,9,10]

#List Comprehension to copy list into another list
my_list = [n*n for n in nums]
print(my_list)

#List Comprehension to copy n values into Different List if n is even
my_list = [n for n in nums if n%2==0]
print(my_list)


#List Comprehension Letter Number pair for each letter in 'abcd' and each number in '0123'
my_list = [ (letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)

#If and Else in LC , Elif can not used in LC
my_list=[x+1 if x>=5 else x+5 for x in nums]
print(my_list)

#If 

for v in nums:
    if v == 1 :
        print('yes')
    else:
        if v == 2:
            print('no')
        else:
            print('idle')
my_list=['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in nums]
for i in my_list:
    print(i)