import math 

#Ryan McVicker
#WARNING THIS WILL CRASH YOUR COMPUTER
# I accidentally wrote this messing around and for some reason this sucked up 
# all the threads in my computer ( Ubuntu 20.04 Focal ) 
def x(numbers) : # pass in array of n length 
    n = len(numbers) 
    for y in numbers:
        numbers.append(y+1) 

if __name__ == '__main__':
    nums = [1,2,3,4] 
    x(x(nums ) ) 

