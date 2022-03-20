# Author = Aslı Yılmaz
# Date = 20.03.2022
# Email = yilmazasl@mef.edu.tr

import sympy as s #Library to use isprime function.
# Since it is not stated whether the library usage is allowed, another isprime function is written in the code.

# The main function will read the input from the file into an integer array.
# Call the functions to find te maximum path
def main():
    numbers = []
    myArr = []

    # Read the input into a 2D integer array "numbers".
    # Each line of the pyramid correspond to a row in the array.
    with open('input.txt', 'r') as file:
        for line in file:
            myArr = line.rstrip().split(" ")  # Line of the pyramid into a string array.
            for i in range(len(myArr)):
                myArr[i] = int(myArr[i])  # Convert the line of the pyramid into an integer array.
            numbers.append(myArr)
            myArr = []  # Empty the array for another line.

    maxsum = 0
    maxpath = []

    # APPROACH 1 : Measures all paths.
    # Since it is only allowed to go from UP-TO-DOWN, any possible path should be measured.
    # If there are N levels of pyramid, there are 2^(N-1) possible paths.
    for i in range(2 ** (len(numbers) - 1)):  # Iterating through every possible paths.
        sum, path = path_sum(numbers, number_to_binary_path(i, len(numbers) - 1))
        if sum > maxsum:  # If new path weight is bigger, assign to the max.
            maxsum = sum
            maxpath = path

    print("APPROACH 1\nSum of the maximum path: ", maxsum, "\nMaximum path from UP-TO-DOWN:")
    print(*maxpath, sep=" > ")

    # APPROACH 2
    maxsum2, maxpath2 = path_sum_2(numbers, 0, 0)
    print("\nAPPROACH 2\nSum of the maximum path:", maxsum2, "\nMaximum path measuring from down: ")
    print(*maxpath2[::-1], sep=" > ")


# Function of APPROACH 1
# Measures the path that given as a binary number.
# 0 is LEFT 1 is RIGHT
# For example, if the binary path is 010 corresponds to LEFT-RIGHT-LEFT
# If there are any prime numbers on te path immediately returns 0
def path_sum(arr, binary_path):
    j = 0
    sum = arr[0][0] #Top of the pyramid
    path = [arr[0][0]]

    for i in range(len(binary_path)):
        if binary_path[i] == 0:# For LEFT
            if isprime(arr[i + 1][j]):
                return 0, []
            sum += arr[i + 1][j]
            path.append(arr[i + 1][j])

        elif binary_path[i] == 1:# For RIGHT
            if isprime(arr[i + 1][j + 1]):
                return 0, []
            sum += arr[i + 1][j + 1]
            path.append(arr[i + 1][j + 1])
            j += 1
    return sum, path

# Function of APPROACH 1
# This function converts the number into binary.
# Then fills the other digits with 0 so that every level has a digit.
def number_to_binary_path(n, level_number):

    binary_path = str(bin(n).replace("0b", ""))

    while len(binary_path) < level_number: # Fill the most significant bits
        binary_path = "0" + binary_path

    return [int(x) for x in binary_path]



# Function of APPROACH 2
# This function recursively calls itself, doesn't return any value till it reaches to the bottom of the pyramid.
# When it reaches the bottom it selects the bigger number that is not prime
# If there are any prime numbers on the path assigns -1 to the path weight and uses it as a flag
def path_sum_2(arr, i, j):

    # If statement for the bottom of the pyramid
    if (i == len(arr)-1):
        if (isprime(arr[i][j])):
            return -1, []
        return arr[i][j], [arr[i][j]]


    rpath, rpatharray = path_sum_2(arr, i + 1, j + 1)

    lpath, lpatharray = path_sum_2(arr, i + 1, j)

    if (lpath > rpath and lpath!=-1 and not isprime(arr[i][j]) ):
        lpath += arr[i][j]
        lpatharray.append(arr[i][j])

    elif (rpath!=-1 and not isprime(arr[i][j]) ):
        rpath += arr[i][j]
        rpatharray.append(arr[i][j])

    if (lpath > rpath):
        return lpath, lpatharray

    return rpath, rpatharray

def isprime(n):
    if (n <= 1):
        return False

        # Check from 2 to sqrt(n)
    for i in range(2, n//2 + 1):
        if (n % i == 0):
            return False

    return True

if __name__ == '__main__':
    main()
