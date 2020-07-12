# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
        # Your code goes here
        sum = 0
        temp = num
        while (temp > 0):
                n = num % 10
                sum = sum + (n ** 3)
                temp //= 10
                print(sum)
        if (num == sum):
                return True
        else:
                return False
