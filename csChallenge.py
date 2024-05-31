'''
Ask the user for a series of integers, one at a time. The user should enter a sentinel value of -99 to signal they are done with data entry.  The integers should be stored in a list as they are entered.  No other processing should be done at the time of data entry.  The data entry can be in the main program, if you'd like, or in a separate function. 
Define a function that is passed the list of integers and gives back the count of odd numbers in the list.  The main program must call the function and use the result, displaying the count to the user. 
Use a commenting style based on what you adopted from previous studies.
'''
#Step 1 - Build list using usr input

# def buildList():
#     usrNums = []
#     usrInput = ""
#     while usrInput != "-99":
#         usrInput = input("Pls insert num. When done input -99 -->")
#         if usrInput != "-99":
#             usrNums.append(int(usrInput))
#     return usrNums
# print(buildList())

#Step 2 - Create function that takes list and counts odds

def countOdd(list):
    count = 0
    for num in list:
        if num % 2 != 0:
            count += 1
    return count
# print(countOdd(buildList()))

# Step 3 - Build function that uses countOdd and prints the return
def main():
    usrNums = []
    usrInput = ""
    while usrInput != "-99":
        usrInput = input("Pls insert num. When done input -99 -->")
        if usrInput != "-99" and int(usrInput) %2 !=0:
            usrNums.append(int(usrInput))
    howMany = countOdd(usrNums)
    print("There are", howMany, "odd nums in your list!")
main()