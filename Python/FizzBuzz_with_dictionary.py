# [FizzBuzz the long way using dictionaries to retrieve the output]
# Author: @Vilma-Agalioti

output_dict={'3':'Fiz z z z z z z',
             '5':'Buz z z z z z z',
            '3-5':'Fi22Bu22'}


for i in range(0, 101):
    
    if (i%3 == 0) and (i%5 ==0): 
        print(i, output_dict['3-5'])
    elif i%3 == 0: 
        print(i, output_dict['3'])
    elif i%5 == 0: 
        print(i, output_dict['5'])
    else:
        print(i)

