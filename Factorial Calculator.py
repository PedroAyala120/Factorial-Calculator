#The user will enter a nonnegative integer and then use a loop to calculate the factorial of that number and display the factorial
#Pedro Ayala

#n is input for the user input of the first factor
n = int(input('input a factor: '))

factor = 1      #Initialize factor to start at 1

#loop to calculate the factorial
for i in range (1, n + 1):
   factor = i * factor

#display the factorial
print ("The factorial of:",n, "is ", factor)
