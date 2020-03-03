# '''Print all Jumping Numbers smaller than or equal to a given value
#
# A number is called as a Jumping Number if all adjacent digits in it differ by 1. The difference between ‘9’ and ‘0’ is not considered as 1.
# All single digit numbers are considered as Jumping Numbers.
# For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.
#
# Given a positive number x, print all Jumping Numbers smaller than or equal to x.'''
#
num = int(input("\nEnter the Number"))

if len(str(num)) == 1:
    print('The Numbers are: ',*(range(0,num+1)),sep='\n')
else:
    print('The Numbers are: ', *(range(0, 10)), sep='\n')

for temp in range(0, num + 1):

    GetNum = str(temp)
    for index in range(0, len(GetNum) - 1):
        difference = int(GetNum[index]) - int(GetNum[index + 1])

        if abs(difference) == 1:
            if index == len(GetNum) - 2:
                print(GetNum)
        else:
            break


