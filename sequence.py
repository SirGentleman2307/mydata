# Make an algorithm that generates the first n number in a sequence
# 1. The algorithm gets a input from the user
# 2. The input is n and that is the number of numbers the user whants
# 3. The algorithm saves 3 number that came be for the n number
# 4. For n number the algorithm prints the summs of the previus 3 numbers
n = int(input("Enter the length of the sequence: "))

num_1 = 1
num_2 = 2
num_3 = 3

for i in range(1, n+1):
    if 1 <= i <= 3:
        print(i)
    else:
        seq_num = num_1 + num_2 + num_3     # find the sum of numbers
        num_1 = num_2                       # update the numbers be for seq_num
        num_2 = num_3
        num_3 = seq_num                     # seq_num becomes the 3 number for the next number
        print(seq_num)