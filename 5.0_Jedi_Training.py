  #Sign your name:________________


print(chr(45))
print(ord("!"))

encrypt=input("enter a word to encrypt")

encrypted=''
for letter in encrypt:
    i=ord(letter)+5
    newletter=chr(i)
    encrypted+=newletter


print("encrypt")












# import random
'''
#  1. Make the following program work.
#    '''
# print("This program takes three numbers and returns the sum.")
# total = 0
#
# for i in range(3):
#     x = int(input("Enter a number: "))
#     total = total + x
# print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
# for i in range (2,101,2):
#     print(i)




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
# done = False
# while not done:
#     print(10,9,8,7,6,5,4,3,2,1,0)
#     print(9)
#     print(8)
#     print(7)
#     print(6)
#     print(5)
#     print(4)
#     print(3)
#     print(2)
#     print(1)
#     print(0)
#     done = True
# print("Blast Off!")





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
# x = random.randint(1,10)
# print(x)




'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
sum = 0

pos = 0

neg = 0

zeros = 0
for i in range(7):
    num=int(input("give me a number "))
    sum+=num
    if num > 0:
        neg+=1
    elif num>0:
        pos+=1
    else:
        zeros+=1
print("--------------------------")
print("             REPORT             ")
print("total: ",sum)
print("total: ",neg)
print("total: ",pos)
print("total: ",zeros)

# for letter in "death star":

# print("The total is:", total)
